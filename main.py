import streamlit as st
import page.insert as insert
import page.select as select
import page.update as update
import page.delete as delete

st.sidebar.title('Menu')
page = st.sidebar.selectbox('Cliente',['Incluir','Consultar','Alterar','Deletar'])

if page == 'Consultar':
    select.consultar()

if page == 'Incluir':
    insert.incluir()

if page == 'Alterar':
    update.alterar()

if page == 'Deletar':
    delete.deletar()