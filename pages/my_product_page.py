import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.Base import Base
from selenium.webdriver.support import expected_conditions as EC

class My_product_page(Base):

    """Locators"""
    add_to_cart = '//span[contains(text(), "В корзину")]'
    go_to_cart = '(//button[@class="e4uhfkv0 css-gh3izc e4mggex0"])[1]'


    """Getters"""
    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))


    """Actions"""

    def click_add_button(self):
        self.get_add_to_cart().click()
        print('Товар добавлен в корзину')

    def click_go_cart_button(self):
        self.get_go_to_cart().click()
        print('Переход в корзину')


    """Methods"""
    def buy_product(self):
        with allure.step('Добавление товара в корзину'):
            self.click_add_button()
            self.click_go_cart_button()
            self.link_assertion('https://www.citilink.ru/order/')