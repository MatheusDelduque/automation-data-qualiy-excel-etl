from selenium import webdriver
from time import sleep
import pytest
import subprocess

@pytest.fixture
def driver():
    # Iniciando o streamlit no background
    process = subprocess.Popen(['streamlit', 'run', 'src/app.py'])
    
    # Iniciando o webdriver usando o GeckoDriver
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(5)
    yield driver

    # Encerrando o streamlit e o webdriver ao final do teste
    process.terminate()
    driver.quit()

def test_app_opens(driver):
    # Verificando se o streamlit foi iniciado corretamente
    driver.get('http://localhost:8501')

def test_check_title_is(driver):
    # Verificando se o streamlit foi iniciado corretamente
    driver.get('http://localhost:8501')
    sleep(5)

    # Pegando o tiulo da página
    page_title = driver.title

    # Verificando se o tiulo da página e o esperado
    expected_title = 'Validador de schemas de Excel'
    assert page_title == expected_title, f"O titulo da pagina deve ser '{expected_title}', mas foi '{page_title}'"