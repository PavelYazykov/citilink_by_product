import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.Base import Base
from selenium.webdriver.support import expected_conditions as EC

class Main_page(Base):


    """Locators"""

    popular_categories = '//span[contains(text(), "Популярные категории")]'
    notebooks = '//a[@data-meta-category="cardId-1"]'


    """Getters"""
    def get_notebooks(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, self.notebooks)))

    def get_popular_categories(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, self.popular_categories)))


    """Actions"""
    def move_popular_categories(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_popular_categories())
        time.sleep(3)
        print('Переход в раздел популярные категории')

    def click_notebooks(self):
        self.get_notebooks()
        self.get_notebooks().click()
        time.sleep(2)
        print('Переход в раздел Ноутбуки')

    """Methods"""
    def choose_goods(self):
        with allure.step('Выбор ноутбука'):
            # self.move_to_news()
            self.move_popular_categories()
            self.click_notebooks()
            self.link_assertion('https://www.citilink.ru/catalog/noutbuki/')




