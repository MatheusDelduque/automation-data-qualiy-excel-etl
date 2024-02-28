import os
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    driver.quit()

def test_check_title_is(driver):
    # Verificando se o streamlit foi iniciado corretamente
    driver.get('http://localhost:8501')
    sleep(5)

    # Pegando o tiulo da página
    page_title = driver.title

    # Verificando se o tiulo da página e o esperado
    expected_title = 'Validador de schemas de Excel'
    assert page_title == expected_title, f"O titulo da pagina deve ser '{expected_title}', mas foi '{page_title}'"
    driver.close()

def test_check_app_h1_is(driver):
    # Verificando se o streamlit foi iniciado corretamente
    driver.get('http://localhost:8501')
    sleep(5)

    # Pegando o h1 da página
    page_h1 = driver.find_element(By.TAG_NAME, "h1").text

    # Verificando se o h1 da página e o esperado
    expected_h1 = 'Insira o arquivo Excel para validação'
    assert page_h1 == expected_h1, f"O h1 da pagina deve ser '{expected_h1}', mas foi '{page_h1}'"
    driver.close()

def test_check_user_can_enter_excel(driver):
    # Verificando se o streamlit foi iniciado corretamente
    driver.get('http://localhost:8501')
    sleep(5)

    # Realizar o upload do arquivo Excel
    success_file_path = os.path.abspath("data/success.xlsx")
    driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(success_file_path)
    sleep(5)

    assert "O schema do arquivo Excel foi validado com sucesso!" in driver.page_source
    driver.close()

def test_failed_upload(driver):
    driver.get('http://localhost:8501')
    sleep(5)

    failure_file_path = os.path.abspath("data/failure.xlsx")
    driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(failure_file_path)
    sleep(5)

    assert "O schema do arquivo Excel foi validado com erro" in driver.page_source