from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.chrome.service import Service

class Base:

    def __init__(self, driver):
        self.driver = driver


    def settings(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)

    def assert_text(self, locator, result):
        value_locator = locator.text
        assert value_locator == result
        print(value_locator)
        print('Good assert')

    def get_current_url(self):
        cur_url = self.driver.current_url()
        print(cur_url)

    def link_assertion(self, result):
        cur_url = self.driver.current_url
        assert cur_url == result
        print(f'Проверка перехода {cur_url} успешно пройдена')





