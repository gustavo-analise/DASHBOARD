import sqlite3
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def setup_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    # Criação das tabelas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS arvores (
            IDARVORE INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            nome TEXT NOT NULL,
            especie TEXT NOT NULL,
            altura INTEGER,
            poda_status TEXT,
            condicao_arvore TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parques (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            nome_parque TEXT NOT NULL,
            local TEXT NOT NULL,
            ano_criado INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parque_arvores (
            parque_id INTEGER NOT NULL,
            arvore_id INTEGER NOT NULL,
            PRIMARY KEY (parque_id, arvore_id),
            FOREIGN KEY (parque_id) REFERENCES parques(id),
            FOREIGN KEY (arvore_id) REFERENCES arvores(IDARVORE)
        )
    """)
    
    conn.commit()

    # Inserindo dados nas tabelas
    arvores = arvores = [
        ("pinheiro-brasileiro", "Araucaria angustifolia", 20, "Precisa podar", "R"),

        ("palmeira-juçara", "Euterpe eduli", 12, "Não precisa podar", "B"),

        ("árvore-da-pataca", "Dillenia indica", 9, "Precisa podar", "R"),

        ("ipê-Amarelo", "Handroanthus sp. Bignoniaceae", 17, "Precisa podar", "P"),

        ("ipê-branco", "Tabebuia roseoalba Bignoniaceae", 15, "Não precisa podar", "B"),

        ("ipê-rosa", "Handroanthus impetiginosus Bignoniaceae", 12, "Precisa podar", "P"),

        ("mandacaru", "Cereus jamacaru", 3, "Não precisa podar", "B"),

        ("seringueira", "Hevea brasiliensis", 30, "Precisa podar", "R"),

        ("flamboyant", "Chloroleucon tortum", 10, "Não precisa podar", "B"),

        ("pau-brasil", "Paubrasilia echinata", 28, "Precisa podar", "P"),

        ("pau-ferro", "Libidibia ferre", 27, "Não precisa podar", "B"),

        ("suinã", "Erythrina speciosa ", 5, "Precisa podar", "P"),

        ("tataré", "Delonix regia", 11, "Precisa podar", "R"),

        ("tipuan", "Tipuana tipu", 12, "Precisa podar", "P"),

        (" jequitibá-rosa","Cariniana legalis",60 ,"Precisa podar","R",),

        ("jequitibá-branco", "Cariniana estrellensis", 50, "Não precisa podar", "B"),

        ("chichá", "Sterculia chicha", 38, "Precisa podar", "P"),

        ("jaboticabeira", "Plinia cauliflor", 7, "Precisa podar", "P"),

        ("melaleuca", "Melaleuca alternifolia", 10, "Não precisa podar", "B"),

        ("eucalipto", "Eucalyptus tereticornis", 38, "Não precisa podar", "B"),

        ("falsa-seringueira", "Ficus elastica", 23, "Não precisa podar", "B"),

        ("figueira-asiática", "Ficus microcarpa", 26, "Precisa podar", "P"),


        ("figueira-de-bengala", "Ficus benghalensis", 22, "Precisa podar", "R"),


        ("cerejeira-japonesa", "Prunus serrulata", 8, "Precisa podar", "R"),


        ("ceboleiro", "Phytolaca dioica", 25, "Precisa podar", "P"),


        ("oliveira", "Olea europaea", 18, "Não precisa podar", "B"),
      
      
      ]

    parques = [
        ("Parque Ibirapuera", "Av. Pedro Álvares Cabral - Vila Mariana", 1954),
        ("Parque Villa-Lobos", "Av. Prof. Fonseca Rodrigues, Alto de Pinheiros", 1994),
    ]

    # Inserir árvores
    for arvore in arvores:
        cursor.execute("""
            INSERT OR IGNORE INTO arvores (nome, especie, altura, poda_status, condicao_arvore)
            VALUES (?, ?, ?, ?, ?)
        """, arvore)

    # Inserir parques
    for parque in parques:
        cursor.execute("""
            INSERT OR IGNORE INTO parques (nome_parque, local, ano_criado)
            VALUES (?, ?, ?)
        """, parque)

    # Inserir associações na tabela intermediária
    parque_arvores = [
        (1, 1),  # Parque Ibirapuera com Pinheiro Brasileiro (IDARVORE 1)
        (1, 2),  # Parque Ibirapuera com Palmeira Juçara (IDARVORE 2)
        (1, 3),  # Parque Ibirapuera com Árvore da Pataca (IDARVORE 3)
        (1, 4),  # Parque Ibirapuera com Ipê Amarelo (IDARVORE 4)
        (1, 5),  # Parque Ibirapuera com Ipê Branco (IDARVORE 5)
        (1, 6),  # Parque Ibirapuera com Ipê Rosa (IDARVORE 6)
        (1, 7),  # Parque Ibirapuera com Mandacaru (IDARVORE 7)
        (1, 8),  # Parque Ibirapuera com Seringueira (IDARVORE 8)
        (1, 9),  # Parque Ibirapuera com Flamboyant (IDARVORE 9)
        (1, 10), # Parque Ibirapuera com Pau-Brasil (IDARVORE 10)
        (1, 11), # Parque Ibirapuera com Pau-Ferro (IDARVORE 11)
        (1, 12), # Parque Ibirapuera com Suinã (IDARVORE 12)
        (1, 13), # Parque Ibirapuera com Tataré (IDARVORE 13)
        (1, 14), # Parque Ibirapuera com Tipuan (IDARVORE 14)
        (1, 15), # Parque Ibirapuera com Jequitibá Rosa (IDARVORE 15)
        (1, 16), # Parque Ibirapuera com Jequitibá Branco (IDARVORE 16)
        (1, 17), # Parque Ibirapuera com Chichá (IDARVORE 17)
        (1, 18), # Parque Ibirapuera com Jaboticabeira (IDARVORE 18)
        (1, 19), # Parque Ibirapuera com Melaleuca (IDARVORE 19)
        (1, 20), # Parque Ibirapuera com Eucalipto (IDARVORE 20)
        (1, 21), # Parque Ibirapuera com Falsa-Seringueira (IDARVORE 21)
        (1, 22), # Parque Ibirapuera com Figueira Asiática (IDARVORE 22)
        (1, 23), # Parque Ibirapuera com Figueira de Bengala (IDARVORE 23)
        (1, 24), # Parque Ibirapuera com Cerejeira Japonesa (IDARVORE 24)
        (1, 25), # Parque Ibirapuera com Ceboleiro (IDARVORE 25)
        (1, 26), # Parque Ibirapuera com Oliveira (IDARVORE 26)
        (2, 1),  # Parque Villa-Lobos com Pinheiro Brasileiro (IDARVORE 1)
        (2, 2),  # Parque Villa-Lobos com Palmeira Juçara (IDARVORE 2)
        (2, 3),  # Parque Villa-Lobos com Árvore da Pataca (IDARVORE 3)
        (2, 4),  # Parque Villa-Lobos com Ipê Amarelo (IDARVORE 4)
        (2, 5),  # Parque Villa-Lobos com Ipê Branco (IDARVORE 5)
        (2, 6),  # Parque Villa-Lobos com Ipê Rosa (IDARVORE 6)
        (2, 7),  # Parque Villa-Lobos com Mandacaru (IDARVORE 7)
        (2, 8),  # Parque Villa-Lobos com Seringueira (IDARVORE 8)
        (2, 9),  # Parque Villa-Lobos com Flamboyant (IDARVORE 9)
]

    cursor.executemany("""
        INSERT OR IGNORE INTO parque_arvores (parque_id, arvore_id)
        VALUES (?, ?)
    """, parque_arvores)

    conn.commit()
    conn.close()

# Função para autenticação de usuários
def authenticate(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users WHERE username = ? AND password = ?
    """, (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Função para registrar usuários
def register_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (username, password) VALUES (?, ?)
        """, (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


# Função para exibir a tabela de árvores com os IDs dos parques correspondentes
def exibir_tabela_arvores_parques():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Consulta para exibir informações de árvores e os parques associados
    cursor.execute("""
        SELECT 
            parques.nome_parque,
            arvores.nome AS Nome_Arvore,
            arvores.especie AS Especie,
            arvores.altura AS Altura,
            arvores.poda_status AS Poda_Status,
            arvores.condicao_arvore AS Condicao_Arvore
        FROM 
            parque_arvores
        JOIN 
            arvores ON parque_arvores.arvore_id = arvores.IDARVORE
        JOIN 
            parques ON parque_arvores.parque_id = parques.id
        ORDER BY 
            parques.nome_parque, arvores.nome
    """)

    # Recupera os dados
    dados = cursor.fetchall()
    conn.close()

    # Separar os dados por parque
    tabelas_por_parque = {}
    for linha in dados:
        parque = linha[0]
        if parque not in tabelas_por_parque:
            tabelas_por_parque[parque] = []
        tabelas_por_parque[parque].append(linha[1:])  # Adiciona os dados sem o nome do parque

    # Exibir uma tabela por parque
    for parque, dados_arvores in tabelas_por_parque.items():
        st.subheader(f"Dados das Árvores - {parque}")
        df = pd.DataFrame(dados_arvores, columns=[
            "Nome da Árvore", "Espécie", "Altura", "Status de Poda", "Condição da Árvore"
        ])
        st.dataframe(df)

def gerar_grafico():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Consulta para contar as condições das árvores por parque
    cursor.execute("""
        SELECT 
            parques.nome_parque, 
            arvores.condicao_arvore, 
            COUNT(*) AS total
        FROM 
            parque_arvores
        JOIN 
            arvores ON parque_arvores.arvore_id = arvores.IDARVORE
        JOIN 
            parques ON parque_arvores.parque_id = parques.id
        GROUP BY 
            parques.nome_parque, arvores.condicao_arvore
    """)
    dados = cursor.fetchall()
    conn.close()

    # Preparar os dados para os gráficos
    condicoes_por_parque = {}
    for parque, condicao, total in dados:
        if parque not in condicoes_por_parque:
            condicoes_por_parque[parque] = {"P": 0, "B": 0, "R": 0}
        condicoes_por_parque[parque][condicao] += total

    legenda_map = {"P": "Péssimo", "B": "Bom", "R": "Ruim"}

    # Gerar os gráficos
    fig, axs = plt.subplots(1, len(condicoes_por_parque), figsize=(12, 6))
    if len(condicoes_por_parque) == 1:
        axs = [axs]  # Garantir que axs seja uma lista se houver apenas um parque

    for i, (parque, condicoes) in enumerate(condicoes_por_parque.items()):
        labels = [legenda_map.get(cond, cond) for cond in condicoes.keys()]
        sizes = list(condicoes.values())
        axs[i].pie(
            sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors
        )
        axs[i].set_title(f"Distribuição das Condições - {parque}")

    st.pyplot(fig)

# Função para exibir os relatórios filtrados
def exibir_relatorios_filtros():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Obter os parques disponíveis (Agora vamos usar o id diretamente)
    cursor.execute("SELECT id, nome_parque FROM parques WHERE id IN (1, 2)")  # Só pega Ibirapuera e Villa Lobos
    parques = cursor.fetchall()
    parque_opcoes = {parque[1]: parque[0] for parque in parques}
    parque_selecionado = st.selectbox("Selecione o parque", ["Todos"] + list(parque_opcoes.keys()))

    # Obter as árvores disponíveis
    cursor.execute("SELECT DISTINCT nome FROM arvores")
    arvores = [arvore[0] for arvore in cursor.fetchall()]
    arvore_selecionada = st.selectbox("Selecione a árvore", ["Todas"] + arvores)

    # Condições disponíveis
    condicoes = {"Todos": None, "Péssimo (P)": "P", "Bom (B)": "B", "Ruim (R)": "R"}
    condicao_selecionada = st.selectbox("Selecione a condição", list(condicoes.keys()))

    # Construir consulta dinâmica com base nos filtros
    query = """
        SELECT 
            parques.nome_parque, 
            arvores.nome AS Nome_Arvore, 
            arvores.especie AS Especie, 
            arvores.altura AS Altura, 
            arvores.poda_status AS Poda_Status, 
            arvores.condicao_arvore AS Condicao_Arvore
        FROM 
            parque_arvores
        JOIN 
            arvores ON parque_arvores.arvore_id = arvores.IDARVORE
        JOIN 
            parques ON parque_arvores.parque_id = parques.id
    """
    conditions = []
    params = []

    # Filtros
    if parque_selecionado != "Todos":
        st.write(f"Filtrando por parque: {parque_selecionado}")  # Depuração
        conditions.append("parques.id = ?")
        params.append(parque_opcoes[parque_selecionado])

    if arvore_selecionada != "Todas":
        conditions.append("arvores.nome = ?")
        params.append(arvore_selecionada)

    if condicoes[condicao_selecionada]:
        conditions.append("arvores.condicao_arvore = ?")
        params.append(condicoes[condicao_selecionada])

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY parques.nome_parque, arvores.nome"

    # Executar consulta
    cursor.execute(query, params)
    dados = cursor.fetchall()
    conn.close()

    # Exibir tabela com os resultados
    if dados:
        df = pd.DataFrame(dados, columns=[
            "Parque", "Nome da Árvore", "Espécie", "Altura", "Status de Poda", "Condição da Árvore"
        ])
        st.dataframe(df)
    else:
        st.write("Nenhum resultado encontrado para os filtros aplicados.")



# Função principal do Streamlit
def main():
    st.title("Sistema de Gestão de Árvores e Parques")

    menu = ["Login", "Registrar", "Dashboard", "Tabelas","Relatórios"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        st.subheader("Login de Usuário")

        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")

        if st.button("Login"):
            user = authenticate(username, password)
            if user:
                st.success(f"Bem-vindo, {username}!")
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
            else:
                st.error("Credenciais inválidas!")

    elif choice == "Registrar":
        st.subheader("Registrar Usuário")

        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")

        if st.button("Registrar"):
            if register_user(username, password):
                st.success("Usuário registrado com sucesso! Faça login.")
            else:
                st.error("Erro: Nome de usuário já existe.")

    elif choice == "Dashboard":
        if "logged_in" in st.session_state and st.session_state["logged_in"]:
            st.subheader("Dashboard")
            st.write("Bem-vindo ao painel principal.")
            gerar_grafico()
        else:
            st.warning("Por favor, faça login para acessar o Dashboard.")

    elif choice == "Tabelas":
        if "logged_in" in st.session_state and st.session_state["logged_in"]:
            st.subheader("Tabelas")
            exibir_tabela_arvores_parques()
        else:
            st.warning("Por favor, faça login para acessar as Tabelas.")
  
  
    elif choice == "Relatórios":
        if "logged_in" in st.session_state and st.session_state["logged_in"]:
            st.subheader("Relatórios")
            exibir_relatorios_filtros()
        else:
            st.warning("Por favor, faça login para acessar os Relatórios.")


if __name__ == "__main__":
    setup_database()
    main()