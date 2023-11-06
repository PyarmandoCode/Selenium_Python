from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#todo estandar
driver = webdriver.Chrome()
driver.get("https://gmail.com")
driver.maximize_window()


correo = driver.find_element(By.NAME,"identifier")
correo.send_keys("armando.eu.ruiz@gmail.com")
correo.send_keys(Keys.ENTER)
#time.sleep(3)
driver.implicitly_wait(10)

clave = driver.find_element(By.NAME,"Passwd")
clave.send_keys("tupasswordpersonal")
clave.send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()


