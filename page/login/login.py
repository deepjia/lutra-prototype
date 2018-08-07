from selenium.webdriver.common.by import By
from main.driver.selenium import Selenium
from main.driver.lackey import Lackey
from page.base import Base


class Login(Base):
    username = By.ID, 'u'
    password = By.ID, 'p'
    submit = By.ID, 'login_button'
    login2 = 'a.png'

    def __init__(self, *args):
        super().__init__(self)
        self.driver = Selenium(*args).driver()
        self.screen = Lackey().screen()

    def login_qq(self, username: str, password: str):
        self.open('aa')
        self.type(username, self.username)
        self.type(password, self.password)
        self.screen.click(self.login2)