import streamlit as st
import controller.cliente as cliente


def incluir():
    st.title('Incluir Dados')
    profissoes = ['Analista de Dados', 'Engenheiro de Dados', 'Cientista de Dados']

    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome')
        input_age = st.number_input(label='Insira a idade', format='%d', step=1)
        input_job = st.selectbox(label='Insira a profissão',
                                 options=profissoes)
        button_submit = st.form_submit_button('Enviar')

        if button_submit:
            cliente.incluir(input_name, input_age, input_job)
            st.success('Cliente incluido com sucesso!!!')

