import streamlit as st
import controller.cliente as cliente

def alterar():
    if "upda" not in st.session_state:
        st.session_state.upda = False

    st.title('Alterar Dados')
    profissoes = ['Analista de Dados', 'Engenheiro de Dados', 'Cientista de Dados']

    update_id = st.number_input(label='Insira o Id', format='%d', step=1)
    button_update_select = st.button('Consultar')

    if button_update_select:
        st.session_state.upda = True

    if st.session_state.upda == True:
        item = cliente.selecionar_id(update_id)[0]
        with st.form(key='update'):
            update_name = st.text_input(label='Insira o nome', value=item[1])
            update_age = st.number_input(label='Insira a idade', format='%d', step=1, value=item[2])
            update_job = st.selectbox(label='Insira a profissão',
                                     options=profissoes,
                                     index=profissoes.index(item[3]))
            button_update = st.form_submit_button('Alterar')

            if button_update:
                cliente.alterar(update_name, update_age, update_job, item[0])
                st.success('Cliente alterado com sucesso!!!')
                st.session_state.upda = False