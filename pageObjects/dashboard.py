from playwright.sync_api import expect

from pageObjects.orderHistoryPage import OrderHistoryPage


class DashboardPage:
    def __init__(self, page):
        self.page = page


    def dashboard_blinking_text(self):
        expect(self.page.locator('.blinkingText')).to_contain_text("Get Shortlisted")


    def order_navigation(self):
        self.page.get_by_role("button", name="ORDERS").click()
        order_history = OrderHistoryPage(self.page)
        return order_history
