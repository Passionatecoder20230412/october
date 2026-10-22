
from selenium import webdriver
from playwright.sync_api import sync_playwright

class TestMatch:
    def test_two(self):
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True)
            context=browser.new_context()
            page=context.new_page()
            page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
            # page.get_by_placeholder('Enter Name').fill("Vijay Anegondi")
            # page.get_by_placeholder('Enter EMail').fill("anegondivijay@gmail.com")
            # print("done"
            table1=page.locator('[id="taskTable"]')
            headers=page.locator('//tr[@id="headers"]//th')
            print(headers.all_text_contents())
            print("*----------------------------------*")
            print(headers.all_text_contents())
            print("*----------------------------------*")
            tbody=page.locator('//table[@id="taskTable"]//tbody//tr')
            print(tbody.all_inner_texts())
            print("*----------------------------------*")
            print(tbody.all_text_contents())
            print("*----------------------------------*")
            for i in range(1,5):
                web=page.locator(f'//tbody[@id="rows"]//tr[{i}]/td[1]').text_content()
                if web=="Chrome":
                    data=page.locator(f'//tbody[@id="rows"]//tr[{i}]/td').all_text_contents()
                    for j in data:
                        if j.endswith("%"):
                            print(f"CPU load of Chrome process: {j}")
                #             Network speed of Chrome process: 2.7 Mbps
                        if j.endswith("Mbps"):
                            print(f"Network speed of Chrome process: {j}")
                # "Memory Size of Firefox process: 40.9 MB"

                if web == "Firefox":
                    data = page.locator(f'//tbody[@id="rows"]//tr[{i}]/td').all_text_contents()
                    for j in data:
                        if j.endswith("MB"):
                            print(f"Memory Size of Firefox process: {j}")
                        if j.endswith("MB/s"):
                            print(f"Disk space of Firefox process: {j}")
                #                 Network speed of Chrome process: 2.7 Mbps


            page2=context.new_page()
            page2.goto("https://testautomationpractice.blogspot.com/")
            page3= context.new_page()
            page3.goto("https://testautomationpractice.blogspot.com/")












