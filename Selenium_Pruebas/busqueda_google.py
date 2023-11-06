from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#todo Inicializar el controlador del navegador (asegurate de tener el controlador en la carpeta scripts de python)
driver = webdriver.Chrome()
#todo Abrir la pagina de Google
driver.get("https://www.google.com")
#todo maximizar el navegador
driver.maximize_window()
#todo Encontrar el campo de busqueda por su nombbre (en el caso de Google es 'q')
campo_busqueda = driver.find_element(By.NAME,"q")
#todo Escribir "Selenium Python" en el campo de Busqueda
campo_busqueda.send_keys("Selenium Python")
#todo Pulsar Enter en la caja campo de busqueda
campo_busqueda.submit()
#todo esperar unos segundos para ver los resultados
time.sleep(9)
#todo guardar los resultados de la busqueda en un archivo png
driver.save_screenshot("resultados_google.png")
driver.close()