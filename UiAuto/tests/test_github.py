
from playwright.sync_api import sync_playwright
def test_github():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://github.com/")
        page.locator('(//*[text()="Sign in"])[2]').click()
        page.locator('[id="login_field"]').fill('Passionatecoder20230412')
        page.locator('[id="password"]').fill('Vijay@8500593340')
        page.locator('[value="Sign in"]').click()
        page.locator('(//*[@data-component="IconButton"])[1]').click()
        page.locator('(//*[text()="All repositories"])[1]').click()
        page.locator('//*[text()="New repository"]').click()
        page.locator('[id="repository-name-input"]').fill('feature_name_test_001')
        page.locator('//*[text()="Create repository"]').click()
        repo=page.locator('[data-targets="git-clone-help.helpTexts"]').text_content()
        print(repo)


