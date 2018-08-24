import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    login_reg_button = By.XPATH, "//*[@text='登录/注册']"

    @allure.step('点击我的页面中登录/注册')
    def click_login_reg(self):
        self.click(self.login_reg_button)
