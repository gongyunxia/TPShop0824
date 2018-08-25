import pytest

from base.base_analyze import analyze_with_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        expect = args["expect"]

        self.page.home_page.click_mine()
        self.page.mine_page.click_login_reg()
        self.page.login_page.input_username(username)
        self.page.login_page.input_password(password)
        self.page.login_page.click_login()
        self.page.login_page.is_toast_exist(expect)

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_miss_part"))
    def test_login_miss_part(self, args):
        username = args["username"]
        password = args["password"]

        self.page.home_page.click_mine()
        self.page.mine_page.click_login_reg()
        self.page.login_page.input_username(username)
        self.page.login_page.input_password(password)
        return not self.page.login_page.is_login_button_enabled()

