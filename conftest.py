

from playwright.sync_api import sync_playwright

def init_page():

    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
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