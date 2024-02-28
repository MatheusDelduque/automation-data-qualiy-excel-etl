import streamlit as st

class ExcelValidatorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        # Titulo da página
        st.set_page_config(
            page_title='Validador de schemas de Excel',
        )

    def display_header(self):
        # Título do App
        st.title('Insira o arquivo Excel para validação')

    def upload_file(self):
        return st.file_uploader('Carregue seu arquivo Excel', type=['xlsx'])

    def display_results(self, result, error):
        if error:
            st.error(f"O schema do arquivo Excel foi validado com erro: {error}")

        else:
            st.success('O schema do arquivo Excel foi validado com sucesso!')