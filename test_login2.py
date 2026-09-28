import json, time, pytest

from playwright.sync_api import Playwright

from pageObjects.login import LoginPage

with open('data/data.json') as json_file:
    cred = json.load(json_file)
    cred_list = cred['credentials']


@pytest.mark.parametrize("new_cred", cred_list) # store the json credentials list into the new_cred
def test_login_parameterize(playwright: Playwright, new_cred):
    browser = playwright.chromium.launch(headless=False)
    browser_context = browser.new_context()
    page = browser_context.new_page()

    user_name = new_cred['user_email'] # take the user_email from json list and store into variable
    user_pass = new_cred['user_password'] # take the user_pass from json list and store into variable

    login = LoginPage(page)
    login.navigation()
    login.login_para(user_name, user_pass) # pass the user_name, user_pass to the page objects method
    login.login_button()

    time.sleep(5)