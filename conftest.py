import pytest
from playwright.sync_api import sync_playwright


# Add a command-line option so you can switch browsers via terminal if needed
def pytest_addoption(parser):
    parser.addoption("--browser-type", action="store", default="chrome", help="Browser: chrome, firefox, or webkit")


@pytest.fixture(scope="function")
def init_page(request):
    # Retrieve the browser option from pytest command line/config
    browser_type = request.config.getoption("--browser-type")

    with sync_playwright() as p:
        if browser_type == "chrome":
            browser = p.chromium.launch(headless=True)
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=True)
        else:
            browser = p.webkit.launch(headless=True)

        context = browser.new_context()
        page = context.new_page()

        # Protect against slow site timeouts (60 seconds)
        page.set_default_navigation_timeout(60000)

        try:
            # wait_until="domcontentloaded" stops tracking scripts from stalling your pipeline
            page.goto("https://automationexercise.com", wait_until="domcontentloaded")
            print(f"\n[Browser: {browser_type}] Page Title: {page.title()}")
        except Exception as e:
            print(f"\nNavigation warning caught: {e}")

        # Yield the clean active page context to your test cases
        yield page

        # Safe explicit teardown sequence
        page.close()
        context.close()
        browser.close()
