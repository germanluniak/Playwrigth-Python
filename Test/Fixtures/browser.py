import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture()
def browser(playwright):
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    yield browser
    browser.close()

@pytest.fixture()
def context(browser):
    context = browser.new_context(
        viewport={
            'width': 2560,
            'height': 1440
        },
    )
    yield context
    context.close()

@pytest.fixture()
def page(context):
    page = context.new_page()
    yield page
    page.close()
