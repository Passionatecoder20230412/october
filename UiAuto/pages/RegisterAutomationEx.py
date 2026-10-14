from UiAuto.pages.basepage import BasePage


class RegisterAutomationEx(BasePage):

    #locators
    HOME_TEXT='//h1//*[contains(text(),"Automation")]'
    SIGNUP='[href="/login"]'
    NEW_USER_FORM='//h2[contains(text(),"New User")]'
    NAME='[placeholder="Name"]'
    EMAIL='[data-qa="signup-email"]'
    SIGNUP_BUTTON='[data-qa="signup-button"]'
    GENDER_MR='[for="id_gender1"]'
    PASSWORD='[data-qa="password"]'
    DAY_DOB='[data-qa="days"]'
    MONTH_DOB='[data-qa="months"]'
    YEAR_DOB='[data-qa="years"]'
    CHKBOX1='[for="newsletter"]'
    CHKBOX2='[for="optin"]'
    FIRST_NAME='[data-qa="first_name"]'
    LAST_NAME='[data-qa="last_name"]'
    COMPANY_NAME='[data-qa="company"]'
    ADDRESS1='[data-qa="address"]'
    ADDRESS2='[data-qa="address2"]'
    COUNTRY='[data-qa="country"]'
    STATE='[data-qa="state"]'
    CITY='[data-qa="city"]'
    ZIPCODE='[data-qa="zipcode"]'
    MOBILE='[data-qa="mobile_number"]'
    CREATE_ACCOUNT='[data-qa="create-account"]'




    def __init__(self, page):
        super().__init__(page)

    def register_automation_ex(self,name,email,password,day_index,month_label,year_val,first_name,last_name,company,address_v,address_m,country_label,state,city,zipcode,mobile):
        # self.inner_data(self.HOME_TEXT)
        self.click_btn(self.SIGNUP)
        self.inner_data(self.NEW_USER_FORM)
        self.fill_data(self.NAME,name)
        self.fill_data(self.EMAIL,email)
        self.click_btn(self.SIGNUP_BUTTON)
        self.page.wait_for_timeout(3000)
        self.check_box(self.GENDER_MR)
        self.fill_data(self.PASSWORD,password)
        self.sel_index(self.DAY_DOB,day_index)
        self.sel_label(self.MONTH_DOB,month_label)
        self.sel_value(self.YEAR_DOB,year_val)
        self.check_box(self.CHKBOX1)
        self.check_box(self.CHKBOX2)
        self.fill_data(self.FIRST_NAME,first_name)
        self.fill_data(self.LAST_NAME,last_name)
        self.fill_data(self.COMPANY_NAME,company)
        self.fill_data(self.ADDRESS1,address_v)
        self.fill_data(self.ADDRESS2,address_m)
        self.sel_label(self.COUNTRY,country_label)
        self.fill_data(self.STATE,state)
        self.fill_data(self.CITY,city)
        self.fill_data(self.ZIPCODE,zipcode)
        self.fill_data(self.MOBILE,mobile)
        self.click_btn(self.CREATE_ACCOUNT)