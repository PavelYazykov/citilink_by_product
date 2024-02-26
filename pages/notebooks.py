import time
import allure
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.Base import Base
from selenium.webdriver.support import expected_conditions as EC

class Notebooks(Base):


    """Locators"""
    product_status = '//div[@class="app-catalog-zdqeii eqp3qu30"]' # focus
    price_slider = '(//div[@class="rc-slider-handle rc-slider-handle-1"])[3]'
    right_price_field = '(//input[@name="input-max"])[3]'
    self_serf = '//span[contains(text(), "Доступен самовывоз")]'
    sale_product = '//span[contains(text(), "Товары со скидкой")]' # focus
    rating = '//span[contains(text(), "4,5 и выше")]'
    apple = '//div[@data-meta-value="APPLE"]'
    my_notebook = '//a[contains(text(), "Ноутбук Apple MacBook Pro")]'
    price_filter = '//button[@data-meta-value="price"]'


    """Getters"""
    def get_product_status(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.product_status)))

    def get_price_slider(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.price_slider)))

    def get_right_price_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.right_price_field)))

    def get_self_serf(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.self_serf)))

    def get_sale_product(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.sale_product)))

    def get_rating(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.rating)))

    def get_apple(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.apple)))

    def get_my_notebook(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.my_notebook)))

    def get_price_filter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.price_filter)))



    """Actions"""

    def focus_product_status(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_product_status())
        print('Переход к Фильтрам')
        time.sleep(1)

    def move_price_slider(self):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.get_price_slider(), 30, 0).perform()
        time.sleep(1)
        print('Выбор цены ползунком')

    def click_right_price_field(self):
        self.get_right_price_field().send_keys(Keys.BACKSPACE*7)
        time.sleep(1)
        self.get_right_price_field().send_keys('350000')
        self.get_right_price_field().send_keys(Keys.RETURN)
        print('Установка верхней границы цены')

    def click_self_serf(self):
        self.get_self_serf().click()
        time.sleep(2)
        print('Выбран самовывоз')

    def focus_sale_product(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_sale_product())
        print('Переход к товарам со скидкой')
        time.sleep(2)

    def select_rating(self):
        self.get_rating().click()
        print('Выбор рейтинга товара')

    def click_apple(self):
        try:
            self.get_apple().click()
            print('Выбран эпл')
        except ElementClickInterceptedException:
            print('Ошибка! ElementClickInterceptedException')
            self.get_apple().click()
            print('Выбран эпл')

    def click_my_notebook(self):
        self.get_my_notebook().click()
        print('Выбор ноутбука')

    def click_price_filter(self):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_price_filter())
        self.driver.execute_script('window.scroll(0, 10)')
        self.get_price_filter().click()
        print('Сортировка по минимальной цене')
        time.sleep(2)
        self.get_price_filter().click()
        print('Сортировка по максимальной цене')
        time.sleep(5)


    """Methods"""
    def notebook_filters(self):
        with allure.step('Нстройка фильтров для выбора ноутбука'):
            self.focus_product_status()
            self.move_price_slider()
            self.click_right_price_field()
            self.click_self_serf()
            self.focus_sale_product()
            self.select_rating()
            self.click_apple()
            time.sleep(2)
            self.click_price_filter()
            self.click_my_notebook()
            # self.link_assertion('https://www.citilink.ru/product/'
            #                     'noutbuk-apple-macbook-pro-i7-16gb-ssd512gb-8gb-16-ips-retina-xdr-engkb-1921953/')# убрал проверку
            # чтобы не упал тест если у вас при сортировке будет другой ноутбук



