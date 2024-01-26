import streamlit as st

# Titulo da página
st.set_page_config(
  page_title='Validador de schemas de Excel',
)

# Título do App
st.title('Insira o arquivo Excel para validação')

arquivo = st.file_uploader('Carregue seu arquivo Excel', type=['xlsx'])

if arquivo:
    st.success('O schema do arquivo Excel foi validado com sucesso!')