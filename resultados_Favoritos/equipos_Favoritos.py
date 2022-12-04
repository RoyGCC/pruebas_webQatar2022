import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class TestEquiposFavoritos():
    def test_equiposFavoritos(self):
        self.driver = webdriver.Chrome('C://selenium-java-4.5.3/chromedriver.exe')
        #Hacemos la pestaña del navegador mas grande
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

        self.driver.get("http://localhost/login")
        self.driver.find_element(By.ID, "email").send_keys("prueba6@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("password1")
        self.driver.find_element(By.NAME, "iniciar").submit()

        self.driver.get("http://localhost/equipo?id=1")
        self.driver.get("http://localhost/api/add-favoritos?id=1")
        self.driver.get("http://localhost/equipo?id=2")
        self.driver.get("http://localhost/api/add-favoritos?id=2")
        self.driver.get("http://localhost/equipo?id=25")
        self.driver.get("http://localhost/api/add-favoritos?id=25")
        self.driver.get("http://localhost/equipo?id=31")
        self.driver.get("http://localhost/api/add-favoritos?id=31")
        self.driver.get("http://localhost/equipo?id=32")
        self.driver.get("http://localhost/api/add-favoritos?id=32")

        self.driver.get("http://localhost/favoritos")

        self.driver.quit()
