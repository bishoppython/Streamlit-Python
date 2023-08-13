import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import streamlit as st
import pandas as pd


# Adiciona um componente HTML personalizado para estilizar o sidebar
st.sidebar.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #FF0000;  /* Substitua #FF0000 pela cor desejada */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# LOGO PAGINA PRINCIPAL

# Carrega a imagem do logo
logo_image = "azul.png"

# Exibe a imagem na página principal
st.image(logo_image, width=250)

# SIDEBAR - CONFIGURAÇÃO

# Exibe a imagem no sidebar
st.sidebar.image(logo_image, use_column_width=True)

# Criação do seletor de opções com ID e Nome
filtro = st.sidebar.selectbox("Filtro", ["RE", "NAME"])

# Verifica a seleção do filtro e exibe as informações correspondentes
if filtro == "RE":
    # Campo para inserir o ID
    id = st.sidebar.text_input("Digite o ID")

    # Verifica se o ID foi inserido
    if id:
        # Exibe as informações correspondentes ao ID
        st.write("Informações para o ID: " + id)
        # Lógica para retornar as informações com base no ID

elif filtro == "NAME":
    # Campo para inserir o Nome
    nome = st.sidebar.text_input("Digite o Nome")

    # Verifica se o Nome foi inserido
    if nome:
        # Exibe as informações correspondentes ao Nome
        st.write("Informações para o Nome: " + nome)
        # Lógica para retornar as informações com base no Nome

# ------------- DADOS QUE SERÃO ENVIADOS DO BANCO -------------------------#
# FALTA NÃO JUSTIFICADA
dados = [
    [3, '01/05/2017'],
    [0, '01/05/2019'],
    [1, '01/05/2022']
]

# DADOS SOBRE DM
dm = [
    [1, '01/05/2017','Não Informado'],
    [2, '01/05/2019','Covid'],
    [1, '01/05/2022','None']
]

# DADOS SOBRE INSS
inss = [
    [1, '01/05/2017'],
    [2, '01/05/2019'],
    [1, '01/05/2022']
]

# DADOS TRIPULANTE
nome = "Patricia Neckzuckert"
funcao = "CO-PILOTO"
data_nascimento = "01/01/1990"
data_admissao = "01/01/2021"
nivel_ingles = "Fluente"
nivel_espanhol = "Intermediario"
nivel_frances = None

# DADOS DE SIMULADOR - Historico Simulador #
media = 9
conceito = 'Aprovado'

# DADOS SIMULADOR - SESSÃO, TIPO, NOTAS DAS PROVAS, DATA, MEDIA, CONCEITO
simulador = [
    ['ERJ M1', 'P1', 3, 3, 3, 3, 3, 4, 3, 3, 3, '23/08/2017',f'{media}', f'{conceito}'],
    ['ERJ M2', 'P2', 3, 3, 3, 3, 3, 3, 3, 4, 3, '15/06/2020',f'{media}', f'{conceito}'],
    ['ERJ M3', 'P3', 3, 3, 3, 3, 3, 3, 3, 3, 4, '10/12/2023',f'{media}', f'{conceito}']
]

# DADOS DOS COMENTÁRIOS

# Dados para a tabela
comentarios = [
    ['Parabéns! Conseguiu!', '23/09/2018'],
    ['Recomendo o piloto!', '12/12/2020'],
]

# DADOS DE ELEVAÇÃO

valor = 1
valorP = '89%'
# Dados para a tabela
elevacao = [
    ['Quant. Realizou o Teorico', f'{valor}'],
    ['Média Prova Teorica', f'{valorP}'],
    ['Média Inicial Sistema', f'{valorP}'],
    ['Média Teorica Geral (S.E.)', f'{valorP}'],
    ['Quant. Reprova Teorica', f'{valor}'],
    ['Quant. Reprova Inicial', f'{valor}'],
    ['Quant. Realização Elevação', f'{valor}'],
    ['Quant. Reprova Candidato', f'{valor}'],
    ['Quant. Reprova ALA', f'{valor}'],
    ['Rating. Reprova Avaliador', f'{valorP}'],
]

# CONFIGURAÇÃO DA PAGINA

centered_title_style = """
    text-align: center;
"""

# ----------------------------- EXIBIÇÃO DOS DADOS ------------------------------------------- #

# Exibir as informações do funcionário
# Exibe o título centralizado
st.markdown(f"<h1 style='{centered_title_style}'>Análise de Elevação de Nível</h1>", unsafe_allow_html=True)

# Carregar e exibir a foto do funcionário
foto = "piloto.jpg"
# Usando st.beta_columns() para criar duas colunas
col1, col2, col3 = st.columns([1,2,1])

#st.subheader("Informações Pessoais")
col1.image(foto, use_column_width=True) # caption="Foto do funcionário",
col2.write(f"Nome: {nome}")
col2.write(f"Função: {funcao}")
col3.write(f"Idade: 32 anos")
col2.write(f"Data de Nascimento: {data_nascimento}")
col2.write(f"Data de Admissão: {data_admissao}")
col3.write(f"Nível de Inglês: {nivel_ingles}")
col3.write(f"Nível de Espanhol: {nivel_espanhol}")
col3.write(f"Nível de Francês: {nivel_frances}")

# Criar um DataFrame do pandas
df = pd.DataFrame(dados, columns=['Quant Falta', 'Data'], index=None)
# Ao utilizar Pandas ele vai apresentar automaticamente um index mesmo inserindo a remoção dele no pandas, pois é um detalhe da biblioteca do streamlit

# Outras informações relevantes
st.subheader("Faltas Não Justificadas")
st.table(df)


# Criar um DataFrame do pandas
df_inss = pd.DataFrame(inss, columns=['Quant. Afastamentos', 'Data'], index=None)
# Outras informações relevantes
st.subheader("Afastamento INSS")
st.table(df_inss)


# Criar um DataFrame com as informações de Afastamento
df = pd.DataFrame(dm, columns=['Quantidade', 'Data', 'Motivo'], index=None)

# Outras informações relevantes
st.subheader("Quant. DM")
st.table(df)

# DADOS DO SIMULADOR
# Criar um DataFrame do pandas
df_sim = pd.DataFrame(simulador, columns=['Tipo de Sessão', 'Sessão', 'AP', 'CM', 'VA',
                                          'VM', 'LI', 'TD','CS', 'CT', 'CO', 'Data', 'Media', 'Conceito Final'], index=None)
# Outras informações relevantes
st.subheader("Historico Simulador")
st.table(df_sim)

# DADOS RELEVANTES PARA ELEVAÇÃO DE NÍVEL
st.subheader("INFORMAÇÕES DE ELEVAÇÃO")

# Criar um DataFrame sobre os DADOS DE ELEVAÇÃO
df_ele = pd.DataFrame(elevacao, columns=['Descrição de Provas/Simulados', 'Valor'], index=None)

st.table(df_ele)

# DADOS DE EXIBIÇÃO DOS COMENTÁRIOS
# Criar um DataFrame do pandas
df_comentario = pd.DataFrame(comentarios, columns=['Comentário', 'Data'], index=None)
st.subheader("Comentários")
st.table(df_comentario)





# -- -- -- EDIÇÃO DE PAGE -- -- -- #
# Remover/Esconder o texto do rodapé
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            <div class="css-cio0dv ea3mdgi1">Desenvolvido por
            <a href="/" target="_blank" class="css-z3au9t ea3mdgi2">Inteligência Operacional</a></div>
            """
#
st.markdown(hide_st_style, unsafe_allow_html=True)
