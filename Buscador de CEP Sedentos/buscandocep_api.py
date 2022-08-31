import numpy as np
import requests
import pandas as pd
import streamlit as st
import time
import json

#st.title('Escolha sua opção')

st.set_page_config(
     page_title="Buscador Sedento de Endereços",
     page_icon="🆔",
     layout="centered",
     initial_sidebar_state="collapsed",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

paginaSelecionada = st.selectbox('Selecione o tipo de Busca', ['Selecione uma opção', 'Via CEP', 'Via UF, Logradouro, Localidade'])

if paginaSelecionada == 'Via CEP':
    st.title("Buscador de Endereços via CEP")

    with st.form(key='Buscandor_endereco'):
        cep = st.text_input(label="Digite o CEP Desejado")
        buscar = st.form_submit_button("Buscar")

        if buscar:
            #Deixando as coisas bonitas hehehe
            with st.spinner('Se aperreia não, que nestante aparece...'):
                time.sleep(3)


            # Tratando Dados

            cep = cep.replace("-", "").replace(".", "").replace(" ", "").replace("A", "")

            # Validando Dados

            if len(cep) == 8:
                link_req = f'https://viacep.com.br/ws/{cep}/json/'
                requisicao = requests.get(link_req)
                # st.write(requisicao.text)
                dic_req = requisicao.json()
                # st.write(dic_req)

                # Bloco de Informações Coletadas do Array
                # cidade = st.write("Cidade:",dic_req['localidade'])
                # rua = st.write("Rua:",dic_req['logradouro'])
                # bairro = st.write("Bairro:",dic_req['bairro'])
                # uf = st.write("UF:",dic_req['uf'])
                # cep_r = st.write("CEP:", dic_req['cep'])
                # ddd = st.write("DDD Local:", dic_req['ddd'])

                # Pandas e Streamlit - Exemplificando utilizando uma chamada randomica

                info = pd.DataFrame(dic_req,(0,1))
                #st.dataframe(info)
                st.table(info)


            else:
                st.write(f'O Cep Digitado: {cep} é invalido!')

elif paginaSelecionada == 'Via UF, Logradouro, Localidade':
    st.title("Buscador de Endereços")

    with st.form(key='Buscador_endereco'):
        uf = st.text_input(label="Digite Estado: ")
        cidade = st.text_input(label="Digite Cidade: ")
        endereco = st.text_input(label="Digite Endereço: ")
        buscar_end = st.form_submit_button("Buscar")

        if buscar_end:
            with st.spinner('Já tô indo, não seja chato...'):
                time.sleep(3)
            # Tratando Dados
            # Validando Dados

            if len(uf) == 2:
                link_requisicao = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'
                requisicao = requests.get(link_requisicao)
                # st.write(requisicao.text)
                dic_req = requisicao.json()

                # Pandas e Streamlit
                info = pd.DataFrame(dic_req)
                st.dataframe(info)
                #st.table(info)

            else:
                st.write(f'O Estado precisa ser Digitado: {uf} está invalido!'
                         f'Precisa ser digitado com apenas duas letras')

elif paginaSelecionada == 'Selecione uma opção':
    with st.spinner('Sem estresse, só um minuto...'):
        time.sleep(5)
        st.error('Desculpe parece que estou trabalhando demais, volta e escolher\n'
                 'outro por favor?', icon="🚨")






