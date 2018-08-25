import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"
    view_pwd_button = By.ID, "com.tpshop.malls:id/img_view_pwd"

    @allure.step('登录页面中：输入用户名')
    def input_username(self, text):
        allure.attach("用户名：", text)
        self.input(self.username_edit_text, text)

    @allure.step('登录页面中：输入密码')
    def input_password(self, text):
        allure.attach("密码：", text)
        self.input(self.password_edit_text, text)

    @allure.step('登录页面中：点击注册按钮')
    def click_login(self):
        self.click(self.login_button)

    @allure.step('判断登录按钮是否可用')
    def is_login_button_enabled(self):
        return self.is_location_enabled(self.login_button)

    @allure.step('登录页面中：点击显示密码')
    def click_view_pwd(self):
        self.click(self.view_pwd_button)
