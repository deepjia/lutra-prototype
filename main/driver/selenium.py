#coding:utf-8
import os
import platform
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Selenium:
    def __init__(self, browser='chrome', bit='64', engine_dir='', headless=True, remote_server=None, remote_browser=None):
        if browser == 'Safari':
            self.driver = webdriver.Safari()
        elif browser == 'Remote':
            kwargs = {
                'command_executor': remote_server,
                'desired_capabilities': getattr(DesiredCapabilities, remote_browser)
            }
            self.driver = webdriver.Remote(**kwargs)
        else:
            # make driver path
            os_name = platform.system()
            driver_dir = {'Darwin': 'mac',
                          'Linux': 'linux',
                          'Windows': 'win'
                          }[os_name] + bit
            driver_file = {'Firefox': 'geckodriver',
                           'Chrome': 'chromedriver',
                           'Ie': 'IEDriverServer'
                           }[browser] + ('.exe' if os_name == 'Windows' else '')
            driver_path = os.path.join(engine_dir, driver_dir, driver_file)
            # ie, firefox, chrome need more parameters
            if browser == 'Ie':
                self.driver = webdriver.Ie(driver_path)
            # Firefox & Chrome
            if browser == 'Firefox':
                options = webdriver.FirefoxOptions()
                options.headless = headless
                self.driver = webdriver.Firefox(
                    executable_path=driver_path, firefox_options=options, log_path='geckodriver.log')
            if browser == 'Chrome':
                options = webdriver.ChromeOptions()
                options.headless = headless
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
                self.driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)