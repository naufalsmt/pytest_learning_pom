from playwright.sync_api import expect

from pageObjects.verifyOrder import VerifyOrder


class OrderHistoryPage:

    def __init__(self, page):
        self.page = page


    def order_history_title(self):
        expect(self.page.locator('.py-5')).to_contain_text("Your Orders")

    def order_history_orders(self, order_id):
        row = self.page.locator("tr").filter(has_text=order_id)  # identify the row contain the order_id
        row.get_by_role("button", name="View").click()  # identify the 'View' button in the row
        view_order = VerifyOrder(self.page)
        return view_order