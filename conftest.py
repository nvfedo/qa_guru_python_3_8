from selene.support.shared import browser
import pytest


@pytest.fixture(autouse=True)
def set_browser():
    #browser.config.hold_browser_open = True
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()