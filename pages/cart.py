import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.Base import Base
from selenium.webdriver.support import expected_conditions as EC


class Cart(Base):
    """Locators"""
    guarante_polis = '(//div[@class="css-m887q5 e161kjbr0"])[1]'
    checkin = '//span[contains(text(), "Перейти к оформлению")]'

    """Getters"""
    def get_guarante_polis(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.guarante_polis)))

    def get_chekin(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.checkin)))

    """Actions"""
    def click_guarante_polis(self):
        self.get_guarante_polis().click()
        print('Выбор полиса продления гарантии')

    def click_checkin_button(self):
        self.get_chekin().click()
        print('Переход к оформлению покупки')

    """Methods"""
    def checkin_product(self):
        with allure.step('Выбор полиса и переход к покупке'):
            self.click_guarante_polis()
            # self.click_protect_polis()
            self.click_checkin_button()
            self.link_assertion('https://www.citilink.ru/order/checkout/')
