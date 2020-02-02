#!/usr/bin/python3
""" Test the page """
import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class Drpdowm(unittest.TestCase):
    """ Unittest for web driver, test dropdown
    """
    @classmethod
    def setUp(self):
        """ Setup the web driver """
        self.driver = webdriver.Firefox(executable_path="/home/oem/Documentos/psl/geckodriver")

    @classmethod
    def tearDown(self):
        """ Close the driver """
        self.driver.quit()
        
    def test_drpdown(self):
        """ Test the dropdown """
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://localhost:5000/")

        driver.find_element_by_id("update-data").click()
        sl = Select(driver.find_element_by_id("list-cities"))
        sl.select_by_visible_text("antioquia")
    
    def test_sendintdata(self):
        """ Send integer data """
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://localhost:5000/")

        driver.find_element_by_id("update-data").click()
        sl = Select(driver.find_element_by_id("list-cities"))
        sl.select_by_visible_text("cundinamarca")
        driver.find_element_by_id("list-cities").send_keys("1")
        driver.find_element_by_id("btn-save-data").click()
    

    def test_sendstrdata(self):
        """ Send string data """
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("http://localhost:5000/")

        driver.find_element_by_id("update-data").click()
        sl = Select(driver.find_element_by_id("list-cities"))
        sl.select_by_visible_text("tolima")
        driver.find_element_by_id("list-cities").send_keys("twentyone")
        driver.find_element_by_id("btn-save-data").click()