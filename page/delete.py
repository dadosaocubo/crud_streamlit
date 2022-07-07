import streamlit as st
import controller.cliente as cliente
import pandas as pd

def deletar():
    if "dele" not in st.session_state:
        st.session_state.dele = False

    st.title('Deletar Dados')

    delete_id = st.number_input(label='Insira o Id', format='%d', step=1)
    button_delete_select = st.button('Consultar')

    if button_delete_select:
        st.session_state.dele = True

    if st.session_state.dele == True:
        item = cliente.selecionar_id(delete_id)[0]
        st.write(item)
        button_delete = st.button('Deletar')

        if button_delete:
            cliente.excluir(item[0])
            st.success('Cliente deletado com sucesso!!!')
            st.session_state.dele = False