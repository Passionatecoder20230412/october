from playwright.sync_api import expect

from UiAuto.pages.FormFillPage import FormFillPage


class TestForm:

    def test_form(self,init_page):

        form=FormFillPage(init_page)

        form.name_field("vijay")
        expect(init_page.locator('[id="name"]')).to_have_value("vijay")
        form.email_field("aneg@gmail.com")
        expect(init_page.locator('[id="email"]')).to_have_value("aneg@gmail.com")
        form.phone_field("maxton")
        form.address_field("kjendkjebfkjb")
        print("Happy ending")