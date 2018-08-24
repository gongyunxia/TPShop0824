import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step('登录页面中：输入用户名')
    def input_username(self, text):
        self.input(self.username_edit_text, text)

    @allure.step('登录页面中：输入密码')
    def input_password(self, text):
        self.input(self.password_edit_text, text)

    @allure.step('登录页面中：点击注册按钮')
    def click_login(self):
        self.click(self.login_button)
