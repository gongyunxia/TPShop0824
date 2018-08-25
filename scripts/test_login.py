import random
from time import sleep

import allure
import pytest
from allure.constants import AttachmentType
from selenium.webdriver.common.by import By

from base.base_analyze import analyze_with_file
from base.base_driver import init_driver
from page.page import Page


def random_password():
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    print(password)
    return password


def show_password_data():
    temp_list = list()
    for i in range(2):
        temp_list.append(random_password())
    print(temp_list)
    return temp_list


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    # def test_login(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #     expect = args["expect"]
    #
    #     self.page.home_page.click_mine()
    #     self.page.mine_page.click_login_reg()
    #     self.page.login_page.input_username(username)
    #     self.page.login_page.input_password(password)
    #     self.page.login_page.click_login()
    #     self.page.login_page.is_toast_exist(expect)
    #
    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_miss_part"))
    # def test_login_miss_part(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #
    #     self.page.home_page.click_mine()
    #     self.page.mine_page.click_login_reg()
    #     self.page.login_page.input_username(username)
    #     self.page.login_page.input_password(password)
    #     assert not self.page.login_page.is_login_button_enabled()

    @pytest.mark.parametrize("password", show_password_data())
    def test_show_password(self, password):
        password_location = (By.XPATH, "//*[@text='%s']" % password)
        self.page.home_page.click_mine()
        self.page.mine_page.click_login_reg()
        self.page.login_page.input_password(password)
        assert not self.page.login_page.is_location_exist(password_location)
        self.page.login_page.click_view_pwd()
        sleep(2)
        allure.attach("显示密码：", self.driver.get_screenshot_as_png(), AttachmentType.PNG)
        assert self.page.login_page.is_location_exist(password_location)
