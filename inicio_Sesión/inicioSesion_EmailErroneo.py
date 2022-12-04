
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
#Hacemos la pestaña del navegador mas grande
driver.maximize_window()
driver.delete_all_cookies()

driver.get("http://localhost/login")
driver.find_element(By.ID, "email").send_keys("prueb6@gmail.com")
driver.find_element(By.ID, "password").send_keys("password1")

driver.find_element(By.NAME, "iniciar").submit()

time.sleep(100)
driver.quit()