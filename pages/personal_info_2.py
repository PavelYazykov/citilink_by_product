import time
import allure
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.Base import Base
from selenium.webdriver.support import expected_conditions as EC

class Personal_info(Base):

    """locators"""
    name_field = '//input[@name="insurance-form_firstName"]'
    surname_field = '//input[@name="insurance-form_lastName"]'
    phone_field = '//input[@name="insurance-form_phone"]'
    email_field = '//input[@name="insurance-form_email"]'
    passport_series_field = '//input[@name="passport-form_series"]'
    passport_number_field = '//input[@name="passport-form_number"]'
    passport_get_field = '//input[@name="passport-form_placeOfIssue"]'
    registration_field = '//input[@name="passport-form_addressOfResidence"]'
    passport_date_field = ('/html/body/div[2]/div/div[2]/div/div/div[1]/'
                           'div/div[1]/div[2]/div/div[2]/div/div[3]/form/div/div[5]/div[2]/div/div/input')
    birth_field = ('/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[1]/'
                   'div[2]/div/div[2]/div/div[3]/form/div/div[6]/div[2]/div/div/input')

    """Getters"""
    def get_surname_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.surname_field)))

    def get_name_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.name_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.phone_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.email_field)))

    def get_passport_series_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.passport_series_field)))

    def get_passport_number_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.passport_number_field)))

    def get_passport_get_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.passport_get_field)))

    def get_registration_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.registration_field)))

    def get_passport_date_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.passport_date_field)))

    def get_birth_field(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH, self.birth_field)))


    """Actions"""

    def send_name_field(self):
        self.get_name_field().click()
        self.get_name_field().clear()
        self.get_name_field().send_keys('Павел')
        print('Введено имя')

    def send_surname_field(self):
        self.get_surname_field().click()
        self.get_surname_field().clear()
        self.get_surname_field().send_keys('Языков')
        print('Введена фамилия')

    def send_phone_field(self):
        self.get_phone_field().click()
        self.get_phone_field().clear()
        self.get_phone_field().send_keys('9007778899')
        print('Введен номер телефона')

    def send_email_field(self):
        self.get_email_field().click()
        self.get_email_field().clear()
        self.get_email_field().send_keys('yapv951@mail.ru')
        print('Введен email')

    def send_passport_series_field(self):
        self.get_passport_series_field().click()
        self.get_passport_series_field().clear()
        self.get_passport_series_field().send_keys('0000')
        print('Введена серия паспорта')

    def send_passport_number_field(self):
        self.get_passport_number_field().click()
        self.get_passport_number_field().clear()
        self.get_passport_number_field().send_keys('111111')
        print('Введен номер паспорта')


    def send_passport_get_field(self):
        self.get_passport_get_field().click()
        self.get_passport_get_field().clear()
        self.get_passport_get_field().send_keys('УВД УВД УВД')
        print('Кем выдан паспорт')

    def send_registration_field(self):
        self.get_registration_field().click()
        self.get_registration_field().clear()
        self.get_registration_field().send_keys('Россия')
        print('Введен адрес регистрации')

    def send_passport_date_field(self):
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", self.get_passport_date_field())
        # self.driver.execute_script('window.scroll(0, 10)')
        self.get_passport_date_field().click()
        self.get_passport_date_field().send_keys(Keys.BACKSPACE*10)
        time.sleep(3)
        self.get_passport_date_field().send_keys('01.01.2010')
        time.sleep(5)
        self.get_passport_date_field().send_keys(Keys.ENTER)
        print('Введена дата выдачи паспорта')

    def send_birth_field(self):
        self.get_birth_field().click()
        self.get_birth_field().send_keys(Keys.BACKSPACE*10)
        time.sleep(3)
        self.get_birth_field().send_keys('01.01.1988')
        self.get_birth_field().send_keys(Keys.ENTER)
        print('Введена дата рождения')

    """Methods"""
    def send_personal_info(self):
        with allure.step('Ввод персональных данных'):
            self.send_name_field()
            self.send_surname_field()
            self.send_phone_field()
            self.send_email_field()
            self.send_passport_series_field()
            self.send_passport_number_field()
            self.send_passport_get_field()
            self.send_registration_field()
            self.send_passport_date_field()
            self.send_birth_field()


