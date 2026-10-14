import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def init_page():

    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
<<<<<<< HEAD
        page=browser.new_page()
        page.goto("https://www.automationexercise.com/")
=======
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://automationexercise.com/")
>>>>>>> 72055cb8d9547732051d558be50b73878607b1e8
        print(page.title())
        yield page
        page.close()
        browser.close()


"""
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
driver.close()
"""
