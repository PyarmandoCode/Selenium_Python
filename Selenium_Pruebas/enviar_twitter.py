from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Configura el controlador del navegador (en este caso, Chrome)
driver = webdriver.Chrome()

# Abre Twitter
driver.get("https://www.twitter.com")

# Espera a que se cargue la página
time.sleep(2)

# Encuentra los campos de usuario y contraseña, e ingresa tus credenciales
username = driver.find_element(By.NAME,"session[username_or_email]")
password = driver.find_element(By.NAME,"session[password]")

username.send_keys("TuNombreDeUsuario")
password.send_keys("TuContraseña")

# Envía el formulario
password.send_keys(Keys.RETURN)

# Espera a que inicie sesión (puedes ajustar el tiempo)
time.sleep(5)

# Realiza alguna acción adicional, como enviar un tweet o interactuar con tu línea de tiempo
# Por ejemplo, aquí puedes tuitear "¡Hola desde Selenium!"
tweet_box = driver.find_element(By.XPATH,'//div[@aria-label="Tweet text"]')
tweet_box.send_keys("¡Hola desde Selenium!")
tweet_button = driver.find_element(By.XPATH,'//div[@data-testid="tweetButtonInline"]')
tweet_button.click()

# Cierra el navegador
driver.quit()
