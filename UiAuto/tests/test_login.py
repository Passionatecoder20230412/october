import time

from UiAuto.TestData.test_data import REGISTRATION_DATA
from UiAuto.pages.LoginPage import LoginPage


class TestLogin:

    def test_login(self,init_page):

        login=LoginPage(init_page)
        login.login_data(REGISTRATION_DATA['reg1']['email'],REGISTRATION_DATA['reg1']['password'])
        print("Vijay Anegondi")
        time.sleep(15)
