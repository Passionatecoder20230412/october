from UiAuto.TestData.test_data import REGISTRATION_DATA
from UiAuto.pages.RegisterAutomationEx import RegisterAutomationEx
from playwright.sync_api import sync_playwright,expect
class TestInvoice:
    def test_invoice(self):
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=False)
            context=browser.new_context()
            page=context.new_page()



            # 1. Launch browser
            page.goto("https://google.com")
            page.wait_for_timeout(30000)
            # 2. Navigate to url 'http://automationexercise.com'
            page.goto("https://automationexercise.com/")
            # 3. Verify that home page is visible successfully
            expect(page.locator("h1").nth(1)).to_have_text("AutomationExercise")
            text=page.locator("h1").nth(1).text_content()
            print(text)
            # 4. Add products to cart
            expect(page.locator('//p[contains(text(),"Madame Top")]').nth(1)).to_have_text("Madame Top For Women")
            page.locator('[href="/product_details/7"]').click()
            page.get_by_role("button",name="Add to cart").first.click()

            # 5. Click 'Cart' button
            page.locator('//u[contains(text(), "View Cart")]').click()
            # 6. Verify that cart page is displayed
            expect(page.locator('//li[contains(text(),"Shopping")]')).to_have_text("Shopping Cart")
            # 7. Click Proceed To Checkout
            page.locator('//a[contains(text(),"Proceed To Checkout")]').click()
            # 8. Click 'Register / Login' button
            page.locator('//u[contains(text(),"Register / Login")]').click()
            # 9. Fill all details in Signup and create account
            page.locator('[data-qa="login-email"]').fill(REGISTRATION_DATA["reg1"]["email"])
            page.get_by_role('textbox',name="password").fill(REGISTRATION_DATA["reg1"]["password"])
            page.locator('[data-qa="login-button"]').click()
            # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
            # 11. Verify ' Logged in as username' at top
            expect(page.locator('//a[contains(text(),"Logged")]')).to_have_text("Logged in as vijay")
            # 12.Click 'Cart' button
            page.locator('[href="/view_cart"]').first.click()
            # 13. Click 'Proceed To Checkout' button
            page.locator('//a[contains(text(),"Proceed To Checkout")]').click()
            # 14. Verify Address Details and Review Your Order
            address=page.locator('//ul').nth(1).text_content()
            print(address)
            # 15. Enter description in comment text area and click 'Place Order'
            page.locator('[name="message"]').fill("Happy Journey Drive slowly")
            page.locator('//a[contains(text(),"Place Order")]').click()
            # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
            # data=[("name_on_card","Vijay Anegondi"),("card_number","4242424242424242"),("cvc","709"),("expiry_month",5),("expiry_year",2028)]
            # for data in data:
            page.locator('[name="name_on_card"]').fill("Vijay Anegondi")
            page.locator('[name="card_number"]').fill("4242424242424242")
            page.locator('[name="cvc"]').fill("709")
            page.locator('[name="expiry_month"]').fill("5")
            page.locator('[name="expiry_year"]').fill("2028")

            # 17. Click 'Pay and Confirm Order' button
            page.locator('[data-qa="pay-button"]').click()
            # 18. Verify success message 'Your order has been placed successfully!'
            tex=page.locator("//h2/b").text_content()
            print(tex)
            assert tex=="Order Placed!"
            # 19. Click 'Download Invoice' button and verify invoice is downloaded successfully.
            page.locator('//a[contains(text(),"Download")]').click()
            # 20. Click 'Continue' button
            page.locator('[data-qa="continue-button"]').click()
            # 21. Click 'Delete Account' button
            # 22. Verify 'ACCOUNT DELETED!' and click 'Continue' button