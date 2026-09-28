import time

from playwright.sync_api import Playwright

from pageObjects.login import LoginPage


def test_login_url(playwright: Playwright, browserInstance): # pass conftest fixture 'browserInstance' where
    # configure the browser type

    login = LoginPage(browserInstance) # pass the conftest fixture into the page objective for run under
    # executing browser
    login.navigation()
    login.login_username()
    login.login_password()
    login.login_button()

    time.sleep(5)
