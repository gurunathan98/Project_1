# Use Pytest using Page Object Model

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Test_Data.data import Guru_Data
from Test_Locators.locators import Guru_Locators
import pytest
import time

class Test_Guru:

    #Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield

    def test_delete_existing_employee(self, boot):
        self.driver.get(Guru_Data().url)
        self.driver.implicitly_wait(10)

        # Login
        self.driver.find_element(by=By.NAME, value=Guru_Locators().username_input_box).send_keys(Guru_Data().username)
        self.driver.find_element(by=By.NAME, value=Guru_Locators().password_input_box).send_keys(Guru_Data().password)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().submit_button).click()
        time.sleep(5)

        # Click PIM Module
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().main_menu_item)
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().main_menu_item_wrapper).click()
        time.sleep(5)

        # Delete existing employee information in PIM Module
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().icon_bi_trash).click()
        self.driver.find_element(by=By.XPATH, value=Guru_Locators().button_icon).click()
        print("Delete existing employee information in PIM & see a message for successful deletion")
        time.sleep(10) 
        