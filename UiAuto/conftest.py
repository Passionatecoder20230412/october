import pytest
from playwright.sync_api import sync_playwright

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def init_page(request):
    browser_name = getattr(request, "param", "chrome")

    with sync_playwright() as p:
        if browser_name == "chrome":
            browser = p.chromium.launch(headless=True)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=True)
        else:
            browser = p.webkit.launch(headless=True)

        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.automationexercise.com/")
        print(page.title())

        yield page

        context.close()
        browser.close()




@pytest.fixture(scope="function")
def save_session():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        context=browser.new_context()
        page=context.new_page()
        # page.goto("https://testautomationpractice.blogspot.com/")
        page.goto("https://www.automationexercise.com/")
        page.locator('//u[contains(text(),"Register / Login")]').click()
        page.locator('[data-qa="login-email"]').fill("vijay.test8500@mail.com")
        page.get_by_role('textbox', name="password").fill("vijay@9876")
        page.locator('[data-qa="login-button"]').click()
        page.context.storage_state(path="storage_state.json")
        print(page.title())
        yield page
        page.close()
        browser.close()




# def home_page():
#     HOME='//h1//*[contains(text(),"Automation")]'
#     page=


"""
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
driver.close()
"""