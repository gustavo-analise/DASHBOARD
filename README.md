# Sistema de Gestão de Árvores e Parques

Este projeto consiste em um sistema de gestão de árvores e parques, desenvolvido utilizando Python, SQLite e Streamlit. O sistema permite o gerenciamento de informações sobre árvores e parques, incluindo dados como nome, espécie, altura, condição e status de poda das árvores, além de informações sobre os parques e suas localizações. O sistema também oferece funcionalidades de autenticação de usuários, visualização de dados em tabelas e gráficos, e geração de relatórios filtrados.

## Visão Geral

O projeto é dividido em três partes principais:

1.  **Configuração do Banco de Dados:**
    * O script `app.py` cria um banco de dados SQLite (`database.db`) e inicializa as tabelas necessárias (`users`, `arvores`, `parques`, `parque_arvores`).
    * Insere dados iniciais nas tabelas para facilitar o uso do sistema.

2.  **Autenticação e Registro de Usuários:**
    * O sistema implementa funcionalidades de login e registro de usuários, permitindo o acesso seguro ao dashboard e às funcionalidades de gestão.

3.  **Interface Streamlit:**
    * O aplicativo `app.py` cria uma interface interativa usando Streamlit, permitindo aos usuários:
        * Visualizar dados sobre árvores e parques em tabelas.
        * Gerar gráficos mostrando a distribuição das condições das árvores por parque.
        * Gerar relatórios filtrados com base em critérios como parque, árvore e condição.

## Funcionalidades

* **Autenticação de Usuários:** Login e registro de usuários para acesso seguro ao sistema.
* **Gestão de Árvores e Parques:** Inserção, visualização e edição de dados sobre árvores e parques.
* **Visualização de Dados:** Exibição de dados em tabelas interativas.
* **Geração de Gráficos:** Visualização da distribuição das condições das árvores por parque.
* **Relatórios Filtrados:** Geração de relatórios com base em filtros selecionáveis.

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **SQLite:** Banco de dados relacional para armazenamento de dados.
* **Streamlit:** Framework para criação de aplicativos web interativos.
* **Pandas:** Biblioteca para manipulação e análise de dados tabulares.
* **Matplotlib:** Biblioteca para criação de gráficos.

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone <URL_do_repositório>
    cd <nome_do_repositório>
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Linux/macOS
    venv\Scripts\activate  # No Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install streamlit pandas matplotlib
    ```

4.  **Execute o aplicativo Streamlit:**
    ```bash
    streamlit run app.py
    ```

## Estrutura do Projeto

gestao_arvores_parques/
├── app.py          # Aplicativo Streamlit
├── database.db      # Banco de dados SQLite
└── README.md      # Documentação do projeto

## Link Do Streamlit
https://dashboard-nczgbr9nmpnqkjvs7mk2pn.streamlit.app/


## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou correções de bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.


## Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).
