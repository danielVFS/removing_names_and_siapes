## Pré-requisitos

- Python 3.8 ou superior
- Dependências listadas no arquivo `requirements.txt`

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/danielVFS/remove_names_and_siapes.git
    cd remove_names_and_siapes
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. Coloque o arquivo de entrada `processos.zip` na raiz do projeto.

2. Certifique-se de que o arquivo `nomes_e_siapes.txt` (contendo a lista de nomes e SIAPEs a serem removidos) está presente na raiz do projeto. Siga o mesmo padrão.

3. Se necessário, altere os seguintes parâmetros no script `main.py`:
    ```python
    names_and_siapes_file = 'nomes_e_siapes.txt'
    input_file = 'processos.zip'
    output_folder = 'arquivos_de_saida'
    ```

4. Execute o script:
    ```bash
    python main.py
    ```
   
5. O script irá gerar uma pasta `arquivos_de_saida` na raiz do projeto contendo os textos processados.
