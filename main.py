import os
import zipfile
from utils import normalize_spaces, generate_combinations_of_name, replace_full_word_ignore_case
from pdfminer.high_level import extract_text


def read_names_and_siapes(names_file):
    names_and_siapes = []
    with open(names_file, 'r', encoding='utf-8') as file:
        for line in file:
            name, siape = line.strip().split(';')

            name_parts = name.lower().strip().split()
            # partial_names = generate_combinations_of_name(name_parts)

            # names_and_siapes.append((partial_names, siape.strip()))
            names_and_siapes.append((name_parts, siape.strip()))
    return names_and_siapes


def extract_pdf_to_text(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error extracting text from PDF {pdf_path}: {e}")
        return ""


def remove_names_and_siapes(original_text, names_and_siapes):
    # normalized_text = normalize_spaces(original_text)
    normalized_text = original_text

    for partial_names, siape in names_and_siapes:
        normalized_text = normalized_text.replace(siape, ' ')

        for partial_name in partial_names:
            normalized_text = replace_full_word_ignore_case(normalized_text, partial_name, ' ')

    return normalized_text


def save_text(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)


def process_pdf_files(pdf_directory, names_and_siapes, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(pdf_directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                text = extract_pdf_to_text(pdf_path)
                cleaned_text = remove_names_and_siapes(text, names_and_siapes)

                output_file_name = os.path.splitext(file)[0] + '.txt'
                output_path = os.path.join(output_folder, output_file_name)
                save_text(cleaned_text, output_path)
                print(f"File processed and saved: {output_path}")


def process_zip(zip_file, names_and_siapes, output_folder):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('temp_pdfs')
    process_pdf_files('temp_pdfs', names_and_siapes, output_folder)

    for root, _, files in os.walk('temp_pdfs'):
        for file in files:
            os.remove(os.path.join(root, file))
    os.rmdir('temp_pdfs')


def main():
    names_and_siapes_file = 'nomes_e_siapes.txt'
    input_file = 'processos.zip'
    output_folder = 'output_text'

    names_and_siapes = read_names_and_siapes(names_and_siapes_file)

    if input_file.endswith('.zip'):
        process_zip(input_file, names_and_siapes, output_folder)
    else:
        print("Invalid input format. Use a PDF or a ZIP file containing PDFs.")


if __name__ == "__main__":
    main()
