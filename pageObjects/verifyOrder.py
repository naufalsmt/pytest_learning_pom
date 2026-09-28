from playwright.sync_api import expect


class VerifyOrder:
    def __init__(self, page):
        self.page = page


    def view_order_detail(self, order_id):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
        expect(self.page.locator(".-main")).to_contain_text(order_id)  # verify the saved order_id is present