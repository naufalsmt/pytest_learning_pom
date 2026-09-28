import pytest

# for parallel test -- require to install pytest-xdist in this project. and while running the test write below
# in the terminal as 'pytest -n auto'. here 'n' is number of workers (browsers) and 'auto' indicates the number
# of the browsers. so here 3 browser open parallely to run all tests in this project

# for reporting in 'html' -- required to install pytest-html in this project. and while running add
# '--html={report file name}'. here report file name should be in 'html' extension. and can give path also

# global fixture to declare the term passing from terminal as '--browser_name' or by default its 'chrome'.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser type"
    )

@pytest.fixture(scope="session")
def new_cred(request):
    return request.param


@pytest.fixture(scope="session")
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name") # declare the browser type coming from terminal
    # while run the test. here global fixture 'request' use to config the browser get option

    # condition written to execute either chrome or firefox which need to declare in terminal
    # like '--broser_name=firefox'
    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # yield is used to execute at the end after execute the test method
    yield page
    context.close()
    browser.close()