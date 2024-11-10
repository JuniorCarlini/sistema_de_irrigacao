# Hydric - Sistema de Irrigação Automática

Hydric é um sistema de irrigação automática projetado para otimizar o uso de água em plantações, jardins e outras áreas que necessitam de irrigação controlada. Com o uso de uma ESP32 para monitoramento e controle e um backend desenvolvido em Django com PostgreSQL, o sistema oferece uma interface robusta para visualização e configuração de dados, permitindo controle preciso dos níveis de umidade do solo, umidade do ar e temperatura do ar, além de controle do uso de água e fertilizantes.

## Visão Geral do Projeto

O projeto Hydric integra sensores de umidade, temperatura e nível de solo para monitoramento remoto e controle da irrigação. O sistema opera de forma autônoma, ativando bombas de irrigação quando os níveis de umidade estão baixos, reduzindo o desperdício de água e promovendo a sustentabilidade no uso de recursos hídricos.

## Funcionalidades

- **Dashboard**: Exibição em tempo real dos dados coletados dos sensores.
- **Histórico**: Armazena e exibe dados históricos para análise de padrões de umidade e temperatura.
- **Sensor de Temperatura do Ar**: Monitora e armazena dados sobre a temperatura ambiente.
- **Sensor de Umidade do Ar**: Monitora e armazena dados sobre a umidade do ar.
- **Sensor de Umidade do Solo**: Monitora e armazena dados sobre a umidade do solo, fundamental para a ativação da irrigação.
- **Uso Diário de Água**: Acompanha o volume de água utilizado diariamente.
- **Histórico de Fertirrigação**: Registro de uso e aplicação de fertilizantes junto à água de irrigação.
- **Configurações**: Permite ajustar parâmetros e calibrar sensores.
- **Sobre**: Informações gerais sobre o sistema e seu propósito.

## Estrutura do Projeto

O projeto consiste em duas partes principais:
1. **Backend Django**: Gerenciamento de dados, processamento de solicitações e armazenamento em banco de dados PostgreSQL.
2. **ESP32**: Coleta de dados dos sensores e envio para o backend via API REST.

## Tecnologias Utilizadas

- **Django**: Framework web em Python, utilizado para criar o backend do sistema.
- **PostgreSQL**: Banco de dados relacional usado para armazenar os dados coletados.
- **ESP32**: Microcontrolador responsável por coletar dados dos sensores e enviar para o backend.
- **Apex Charts (Frontend)**: Para construção de gráficos.
- **Bootstrap (Frontend)**: Para construção de elementos interativos na interface do usuário.


## Estrutura do Código

### Backend

O backend, desenvolvido em Django, é responsável por:
- Receber os dados dos sensores enviados pela ESP32.
- Armazenar e processar os dados para relatórios e controle de irrigação.
- Expor APIs RESTful para comunicação com o frontend.

### ESP32

O código da ESP32 está disponível no [repositório do GitHub](https://github.com/JuniorCarlini/sistema-de-irrigacao-esp32) e realiza:
- Leitura dos sensores de umidade do solo, umidade do ar e temperatura.
- Envio dos dados para o backend através de solicitações HTTP.
- Controle de ativação das bombas de irrigação com base nos dados de umidade do solo.

## Configuração e Instalação

### Pré-requisitos

- Python 3.8+ e Django
- PostgreSQL
- Placa ESP32 com sensores de umidade e temperatura

### Configuração do Banco de Dados

1. Instale o PostgreSQL e crie um banco de dados para o projeto.
2. Configure as credenciais de conexão no arquivo `settings.py` do Django:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'hydric_db',
           'USER': 'seu_usuario',
           'PASSWORD': 'sua_senha',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Executando o Projeto

1. Clone o repositório do projeto e instale as dependências:

   ```bash
   git clone https://github.com/JuniorCarlini/hydric.git
   cd hydric
   pip install -r requirements.txt
   ```

2. Execute as migrações para criar as tabelas no banco de dados:

   ```bash
   python manage.py migrate
   ```

3. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

4. Acesse o painel administrativo em `http://127.0.0.1:8000/admin` para gerenciar os dados.

### Configuração da ESP32

Siga as instruções no [repositório do código da ESP32](https://github.com/JuniorCarlini/sistema-de-irrigacao-esp32) para configurar a conexão com os sensores e o envio de dados para o backend.

## API REST

O sistema utiliza endpoints RESTful para comunicação com a ESP32. Principais endpoints incluem:
- `POST /api/temperatura/`: Recebe dados do sensor de temperatura.
- `POST /api/umidade_ar/`: Recebe dados do sensor de umidade do ar.
- `POST /api/umidade_solo/`: Recebe dados do sensor de umidade do solo.
- `GET /api/dashboard/`: Retorna os dados para exibição no dashboard.

## Sobre

Hydric é um projeto dedicado a promover a sustentabilidade na agricultura através de um controle eficiente da irrigação. Seu principal objetivo é reduzir o desperdício de água e otimizar o uso de recursos para beneficiar produtores e o meio ambiente.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou uma issue para sugestões e melhorias.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
