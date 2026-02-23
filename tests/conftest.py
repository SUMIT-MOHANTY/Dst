import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    # Mock reduced motion testing
    page.emulate_media(reduced_motion='reduce')
    yield page
    page.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1280, "height": 720}}
