from pygments.lexers import web

from pageObjects.dashboard import DashboardPage


class LoginPage:


    def __init__(self, page): # here page is connecting with test function with this constructor to use for this class
        self.page = page # declare the page object within the constructor to use in this class


    def navigation(self):
        self.page.goto("https://rahulshettyacademy.com/client")


    def login_username(self):
        self.page.get_by_placeholder("email@example.com").fill("alexis@mail.com")


    def login_password(self):
        self.page.locator("#userPassword").fill("Alex@12345")


    def login_button(self):
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = DashboardPage(self.page)
        return dashboard_page

    def login_para(self, user_name, user_pass): # connect the 'Json' list variable with test file
        self.page.get_by_placeholder("email@example.com").fill(user_name)
        self.page.locator("#userPassword").fill(user_pass)
