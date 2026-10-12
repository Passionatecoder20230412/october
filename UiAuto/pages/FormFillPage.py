from UiAuto.pages.basepage import BasePage


class FormFillPage(BasePage):
    #locators
    NAME='[id="name"]'
    EMAIL='[id="email"]'
    PHONE='[id="phone"]'
    ADDRESS='[id="textarea"]'

    def name_field(self,name):
        self.fill_data(self.NAME,name)
        self.input_data(self.NAME)
    def email_field(self,email):
        self.fill_data(self.EMAIL,email)
        self.input_data(self.EMAIL)
    def phone_field(self,phone):
        self.fill_data(self.PHONE,phone)
        self.input_data(self.PHONE)
    def address_field(self,address):
        self.fill_data(self.ADDRESS,address)
        self.input_data(self.ADDRESS)