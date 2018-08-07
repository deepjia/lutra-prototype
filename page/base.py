class Base:
    def __init__(self, driver, base_url: str='', timeout: int=20):
        self.driver = driver
        self.base_url = base_url
        self.timeout = timeout

    def open(self, url: str):
        url = self.base_url + url
        self.driver.get(url)
        assert self.driver.current_url == url


    def type(self, text, *locator):
        return self.driver.find_element(*locator).sendKeys(text)


    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def snapshot(self, filename: str):
        self.driver.save_screenshot(filename)
