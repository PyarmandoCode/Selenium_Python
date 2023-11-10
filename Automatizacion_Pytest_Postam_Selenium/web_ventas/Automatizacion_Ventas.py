import time

import pytest
from selenium import webdriver
from app import app
from selenium.webdriver.common.by import By

#todo Ciclo de Vida de desarrollo de Software
#todo Pruebas Automatizadas --DEV --QA --PROD --MONIT

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def browser():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()

def test_home_route(client,browser):
    # todo simular navegar a la pagina principal
    browser.get('http://localhost:5000/')
    time.sleep(3)
    # todo Verificar que el titulo de la pagina sea correcta
    assert browser.title=='Flask App'

    # todo Verificar que el encabezado h1 contenga el texto esperado
    h1_element=browser.find_element(By.TAG_NAME,"h1")
    assert h1_element.text == '!Hola , Bienvenidos a mi sitio de ventas!'










