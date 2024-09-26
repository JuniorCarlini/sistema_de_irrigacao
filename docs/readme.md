# Sistema de Irrigação Automatizado

Este é um aplicativo Django para armazenar dados de sensores e exibir um dashboard de monitoramento.

## Funcionalidades

- Armazenamento de dados dos sensores
- Dashboard de exibição dos dados

## Tecnologias Utilizadas

- Django
- SQLite 
- HTML/CSS/JavaScript para o frontend

## Diagrama Elétrico


![
Diagrama Elétrico](docs/image/eletrical_diagram.jpg)


- Django
- SQLite 
- HTML/CSS/JavaScript para o frontend

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/sistema_de_irrigacao_automatizado.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd sistema_de_irrigacao_automatizado
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No Linux/Mac:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
6. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
7. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Uso

Acesse o dashboard no navegador através do endereço `http://127.0.0.1:8000`.

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
