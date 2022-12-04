#Flujo Normal para la creación de la cuenta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
#Hacemos la pestaña del navegador mas grande
driver.maximize_window()
driver.delete_all_cookies()

#Comienza la prueba
driver.get("http://localhost/registrar")
driver.find_element(By.ID, "first_name").send_keys("flujonormal1")
driver.find_element(By.ID, "last_name").send_keys("flujonormal")
driver.find_element(By.ID, "email").send_keys("prueba4@gmail.com")
driver.find_element(By.ID, "password").send_keys("password1")
driver.find_element(By.ID, "repeat_password").send_keys("password1")
driver.find_element(By.NAME, "create").submit()

#Termina la prueba

#Resultado esperado: Se ha creado la cuenta
time.sleep(100)
driver.quit()