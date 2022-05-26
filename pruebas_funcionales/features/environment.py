from behave import fixture, use_fixture
from selenium import webdriver

@fixture
def browser_chrome(context):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    
    context.url = 'http://127.0.0.1:8000'
    yield context.driver
    context.driver.quit()
    
def before_all(context):
    use_fixture(browser_chrome, context)
    
    