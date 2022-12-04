import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TestquitarFavoritos():
    def test_quitarfavoritos(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        #Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.NAME, "iniciar").submit()

        self.driver.get("http://localhost/favoritos")
        self.driver.get("http://localhost/api/delete-favoritos?id=35")
        self.driver.get("http://localhost/favoritos")
        time.sleep(10)
        self.driver.quit()