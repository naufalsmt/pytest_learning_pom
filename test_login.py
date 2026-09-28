import time
from playwright.sync_api import Playwright
from pageObjects.login import LoginPage
from utils.create_order import ApiUtils


def test_login(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    order = ApiUtils()
    order_id = order.create_order(playwright)

    login = LoginPage(page) # connect the class from pageObject
    login.navigation() # this call page.goto("https://rahulshettyacademy.com/client") from pageObjects navigation method
    login.login_username() # this call username action from pageObject enter username method
    login.login_password() # this call username action from pageObject enter password method

    dashboard_page = login.login_button() # this call login button action from pageObject enter login button method
    dashboard_page.dashboard_blinking_text()

    order_history = dashboard_page.order_navigation()
    order_history.order_history_title()

    view_order = order_history.order_history_orders(order_id)
    view_order.view_order_detail(order_id)



    time.sleep(5)