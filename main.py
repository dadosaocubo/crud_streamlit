# carregando as bibliotecas
import streamlit as st
# carregando as funções em outros arquivos .py
import page.insert as insert
import page.select as select
import page.update as update
import page.delete as delete


# criando a barra lateral do menu
st.sidebar.title('Menu')
page = st.sidebar.selectbox('Cliente',['Inserir','Consultar','Alterar','Deletar'])
st.sidebar.markdown('Desenvolvido por: **Tiago Dias**')
st.sidebar.markdown('Email para contato:')
st.sidebar.markdown('diasctiago@gmail.com')
st.sidebar.markdown('LinkedIn:')
st.sidebar.markdown('https://www.linkedin.com/in/diasctiago')
st.sidebar.markdown('GitHub:')
st.sidebar.markdown('https://github.com/diasctiago')

# carregando as páginas de acordo com a seleção do menu
if page == 'Consultar':
    select.consultar()
if page == 'Inserir':
    insert.inserir()
if page == 'Alterar':
    update.alterar()
if page == 'Deletar':
    delete.deletar()