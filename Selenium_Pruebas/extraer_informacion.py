from selenium import  webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://en.wikipedia.org/wiki/Main_Page"
browser.get(url)

cantidad_articulos = browser.find_element(By.CSS_SELECTOR,"#articlecount a")
print(cantidad_articulos.text)
browser.close()

