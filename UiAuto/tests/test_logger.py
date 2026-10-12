import logging
import os
from playwright.sync_api import Page, expect

# 1. CONFIGURE THE LOGGER
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("logs/test_run.log", mode="a"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("PlaywrightTest")


# 2. FIXED TEST LOGIC
def test_dialog_handling(init_page):
    logger.info("Starting test: test_dialog_handling")
    page = init_page

    try:
        url = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"
        logger.info(f"Navigating to browser page: {url}")
        page.goto(url)

        prompt_text = "Hello World"

        # Define a clean, standalone handler function for logging and accepting the dialog
        def handle_dialog(dialog):
            logger.info(f"Dialog event intercepted! Type: {dialog.type}, Default value: {dialog.default_value}")
            dialog.accept(prompt_text=prompt_text)
            logger.info(f"Dialog successfully accepted with text: '{prompt_text}'")

        # Register the listener on the page framework
        logger.info("Registering background listener for JavaScript dialog box...")
        page.on("dialog", handle_dialog)

        # Use expect_event cleanly without the invalid 'handler' parameter
        logger.info("Awaiting the dialog event block...")
        with page.expect_event("dialog"):
            logger.info("Clicking the prompt trigger button...")
            page.locator('[id="promptBtn"]').click()

        logger.info("Dialog flow context completed successfully.")

    except Exception as e:
        logger.error(f"Test failed during execution. Error details: {str(e)}", exc_info=True)
        raise e
