import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    mine_button = By.XPATH, "//*[@text='我的']"
    # @id='com.tpshop.malls:id/tab_txtv'

    @allure.step('点击首页中我的')
    def click_mine(self):
        self.click(self.mine_button)
