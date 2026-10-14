import time

from UiAuto.TestData.test_data import REGISTRATION_DATA
from UiAuto.pages.LoginPage import LoginPage


class TestLogin:

    def test_login(self,init_page):

        login=LoginPage(init_page)
        login.login_data("vijay.test_20261014_135928@mail.com","vijay@9876")
        print("Vijay Anegondi")
        time.sleep(15)
