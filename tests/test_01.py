import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import ChromiumOptions
from base.Base import Base
from selenium.webdriver.chrome.service import Service

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.notebooks import Notebooks
from pages.my_product_page import My_product_page
from pages.cart import Cart
from pages.personal_info_2 import Personal_info


@allure.description('Начало теста покупки ноутбука')
def test_start():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    lp = Login_page(driver)
    lp.authorization()

    mp = Main_page(driver)
    mp.choose_goods()

    n = Notebooks(driver)
    n.notebook_filters()

    mp_p = My_product_page(driver)
    mp_p.buy_product()

    cart = Cart(driver)
    cart.checkin_product()

    time.sleep(3)
    pi = Personal_info(driver)
    pi.send_personal_info()

    print('Тест завершен успешно!')





