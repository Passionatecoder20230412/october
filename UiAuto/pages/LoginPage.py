from UiAuto.pages.basepage import BasePage


class LoginPage(BasePage):
    """
    loginpage locators and methods here
    """
    #locators
    NAV_LOGIN='[href="/login"]'
    EMAIL_FIELD = '[data-qa="login-email"]'
    PASSWORD_FIELD = '[data-qa="login-password"]'
    BUTTON_LOGIN = '[data-qa="login-button"]'



    def login_data(self,email,password):

        self.click_btn(self.NAV_LOGIN)
        self.fill_data(self.EMAIL_FIELD,email)
        self.fill_data(self.PASSWORD_FIELD, password)
        self.click_btn(self.BUTTON_LOGIN)

