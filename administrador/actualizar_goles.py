#Flujo Normal para la creación de la cuenta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C://Users/Roy Carrington/Downloads/chromedriver_win32/chromedriver.exe')
#Hacemos la pestaña del navegador mas grande
driver.maximize_window()
driver.delete_all_cookies()

#Comienza la prueba
driver.get("http://localhost/admin/partidos")
#inicio sesion como administrador
driver.find_element(By.ID, "email").send_keys("roycarrington20@gmail.com")
driver.find_element(By.ID, "password").send_keys("12345678")
driver.find_element(By.NAME, "iniciar").submit()
#actualizacion de goles
driver.find_element(By.NAME or By.ID, "editar").click()
driver.find_element(By.ID, "first_team_goals").send_keys("8")
driver.find_element(By.ID, "second_team_goals").send_keys("9")
driver.find_element(By.NAME, "actualizar").click()


#Termina la prueba

#Resultado esperado: Se actualizaron los goles
time.sleep(5000)
#driver.quit()