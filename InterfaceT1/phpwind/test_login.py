# coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import unittest
from phpwind.login import *


# Login类继承TestCase类，告诉unittest，这是一个案例
class Login(unittest.TestCase):
    # 初始化数据
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implcitly_wait(30)
        self.url = "http://dhw.lxhbysn.com/pages/E02/login.jsp"
        self.verificationErrors = []
        self.accept_next_alert = True

    # 登录
    def test_login(self):
        driver = self.driver
        driver.get(self.url)

    # 调用登录模块
    login.login(self)
    sleep(3)
    lis = driver.find_elements_by_class_name("li")
    for li in lis:
        if li.get_attribute("role") == "presentation":
            print
            li.text

    #
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if _name_ == "_main_":
    unittest.main() 