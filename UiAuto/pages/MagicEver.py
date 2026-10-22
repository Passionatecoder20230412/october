
from selenium import webdriver
from playwright.sync_api import sync_playwright

class TestMatch:
    # def __init__(self):
    #     pass
    def test_one(self):
        driver=webdriver.Chrome()
        driver.get("https://testautomationpractice.blogspot.com/")
        print("done")
    def test_two(self):
        with sync_playwright() as p:
            browser=p.chromium.launch()
            context=browser.new_context()
            page=context.new_page()
            page.goto("https://testautomationpractice.blogspot.com/")
            page.get_by_placeholder('Enter Name').fill("Vijay Anegondi")
            page.get_by_placeholder('Enter EMail').fill("anegondivijay@gmail.com")
            print("done")





