import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management_for_hw():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 3
    # browser.config.browser_name = 'chrome' # and 'firefox' and 'edge' #or 'opera'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
