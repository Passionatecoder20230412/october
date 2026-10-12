

class BasePage:
    def __init__(self,page):
        self.page=page
    def fill_data(self,locator,data):
        self.page.locator(locator).fill(data)
    def inner_data(self,locator):
        text=self.page.locator(locator).inner_text()
        print(text)
    def input_data(self,locator):
        input=self.page.locator(locator).input_value()
        print(input)

    def click_btn(self,locator):
        self.page.locator(locator).click()

    def sel_value(self,locator,text):
        sel=self.page.locator(locator)
        sel.select_option(value=text)
    def sel_label(self,locator,text):
        sel=self.page.locator(locator)
        sel.select_option(label=text)
    def sel_index(self,locator,text):
        sel=self.page.locator(locator)
        sel.select_option(index=text)
    def check_box(self,locator):
        self.page.check(locator)





