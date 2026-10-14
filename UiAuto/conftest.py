import pytest
from playwright.sync_api import sync_playwright

# 1. Add a command-line option so you can switch browsers via terminal if needed
def pytest_addoption(parser):
    parser.addoption("--browser-type", action="store", default="chrome", help="Browser: chrome, firefox, or webkit")

@pytest.fixture(scope="function")
def init_page(request):
    # Retrieve the browser option from pytest command line/config
    browser_type = request.config.getoption("--browser-type")
    
    with sync_playwright() as p:
        if browser_type == "chrome":
            browser = p.chromium.launch(headless=False)
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=False)
        else:
            browser = p.webkit.launch(headless=False)
            
        context = browser.new_context()
        page = context.new_page()
        
        # Protect against slow site timeouts
        page.set_default_navigation_timeout(60000)
        
        try:
            page.goto("https://www.automationexercise.com/", wait_until="domcontentloaded")
            print(f"\n[Browser: {browser_type}] Page Title: {page.title()}")
        except Exception as e:
            print(f"\nNavigation warning caught: {e}")
            
        # FIX: Yield and teardown are now outside the conditional blocks so they ALWAYS run
        yield page
        
        page.close()
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def save_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        page.set_default_navigation_timeout(60000)
        
        try:
            page.goto("https://www.automationexercise.com/", wait_until="domcontentloaded")
            page.locator('//u[contains(text(),"Register / Login")]').click()
            page.locator('[data-qa="login-email"]').fill("vijay.test8500@mail.com")
            page.get_by_role('textbox', name="password").fill("vijay@9876")
            page.locator('[data-qa="login-button"]').click()
            
            # Save authentication state
            context.storage_state(path="storage_state.json")
            print(f"\nSession saved successfully. Page Title: {page.title()}")
        except Exception as e:
            print(f"\nSession generation failed: {e}")
            
        yield page
        
        page.close()
        context.close()
        browser.close()
