# import time
# import allure
# from selenium import webdriver
# from selenium.common import ElementClickInterceptedException
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from base.Base import Base
# from selenium.webdriver.support import expected_conditions as EC
#
# class Personal_info(Base):
#
#     """locators"""
#     add_personal_info_button = ('/html/body/div[2]/div/div[2]/div/div/div[1]/'
#                                 'div/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/button')
#     safer_info = '(//button[@class="css-1qkge9l ek97e1d0"])[1]'
#     name_field = '/html/body/div[9]/div/div/div/div/div[2]/div/div/form/div/div[2]/div[1]/div/div/label/input'
#     surname_field = '//input[@name="RecipientForm__last-name"]'
#     phone_field = '(//input[@name="input-validation-field"])[1]'
#     create_button = '//button[@data-meta-name="RecipientForm__action-button"]'
#     self_serf_point = '//button[@class="e4uhfkv0 css-1w7mt1x e4mggex0"]'
#     my_self_serf = '(//button[@class="e1tiqnd20 css-18kees1 e4mggex0"])[1]'
#
#     """Getters"""
#     def get_add_personal_info_button(self):
#         return WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(
#             (By.XPATH, self.add_personal_info_button)))
#
#     def get_safer_info(self):
#         return WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(
#             (By.XPATH, self.safer_info)))
#
#     def get_surname_field(self):
#         return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
#             (By.XPATH, self.surname_field)))
#
#     def get_name_field(self):
#         return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
#             (By.XPATH, self.name_field)))
#
#     def get_phone_field(self):
#         return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
#             (By.XPATH, self.phone_field)))
#
#     def get_create_button(self):
#         return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
#             (By.XPATH, self.create_button)))
#
#     def get_self_serf_point(self):
#         return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
#             (By.XPATH, self.self_serf_point)))
#
#     def get_my_self_serf(self):
#         return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(
#             (By.XPATH, self.my_self_serf)))
#
#
#     """Actions"""
#     def click_add_personal_info_button(self):
#         self.get_add_personal_info_button().click()
#         print('Ввод данных покупателя')
#
#     def click_safer_info(self):
#         self.get_safer_info().click()
#         print('Ввод данных страхователя')
#
#     def send_name_field(self):
#         self.get_name_field().send_keys('Павел')
#         print('Введено имя')
#
#     def send_surname_field(self):
#         self.get_surname_field().send_keys('Языков')
#         print('Введена фамилия')
#
#     def send_phone_field(self):
#         self.get_phone_field().send_keys('9007778899')
#         print('Введен номер телефона')
#
#     def click_create_button(self):
#         self.get_create_button().click()
#         print('Создать получателя')
#
#     def choose_self_serf_point(self):
#         self.get_self_serf_point().click()
#         print('Выбор пункта самовывоза')
#
#     def choose_my_self_serf(self):
#         self.get_my_self_serf().click()
#         print('Выбран мой пункт самовывоза')
#
#
#     """Methods"""
#     def send_personal_info(self):
#         try:
#             self.click_add_personal_info_button()
#             self.click_safer_info()
#             self.send_name_field()
#             self.send_surname_field()
#             self.send_phone_field()
#             self.click_create_button()
#             self.choose_my_self_serf()
#         except ElementClickInterceptedException:
#             pass
#
#
#
#
#
