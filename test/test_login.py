from main.driver.selenium import Selenium
from page.login.login import Login

class TestCase1:
    def set_up(self):
        self.driver = Login().driver

    def login_pass(self):
        self.login_qq()