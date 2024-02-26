import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.Base import Base
from selenium.webdriver.support import expected_conditions as EC


class Login_page(Base):

    my_login = 'yapv951@mail.ru'
    my_password = '123456789qwerty'
    url = 'https://www.citilink.ru/'
    text_info = '(//span[contains(text(), "Павел")])[1]'


    """Locators"""
    enter_button = '(//span[contains(text(), "Войти")])[1]'
    login_field = '//input[@name="login"]'
    password_field = '//input[@name="pass"]'
    login_button = '(//button[contains(@class, "e4mggex0")])[119]'


    """Getters"""

    def get_text_info(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, self.text_info)))
    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_login_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    """Actions"""

    def click_enter_button(self):
        self.get_enter_button().click()
        print('Вход')

    def send_login(self):
        self.get_login_field().send_keys('yapv951@mail.ru')
        print('Ввод логина')

    def send_password(self):
        self.get_password_field().send_keys('123456789qwerty')
        print('Ввод пароля')

    def click_login_button(self):
        self.get_login_button().click()
        print('Авторизация')

    """Methods"""
    def authorization(self):
        with allure.step('Авторизация'):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_enter_button()
            self.send_login()
            self.send_password()
            self.click_login_button()
            self.assert_text(self.get_text_info(), 'Павел')
            print('Вход в личный кабинет')
