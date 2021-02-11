"""
`params['project_url']` will be returned after deploying the application in docker container. So this will be
available in the params parameter in every function and class methods. For E2E testing, Chrome browser driver path is
available in `params['driver_remote_url']`. See below, are examples to write test cases.

1. Method based
def test_add_to_cart(params):
    project_url = params['project_url']
    driver_path = params['driver_path']
    # ...
    # Your code goes here
    # ...


2. Class based
class Test:
    def test_add_to_cart(self, params):
        project_url = params['project_url']
        driver_remote_url = params['driver_remote_url']
        # ...
        # Your code goes here
        # ...


todo: Only headless option
todo: Create webapp class for browser driver
todo: need to check this on server
"""
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_home_page_worked(params):
    """
    Test RESTful API endpoint to check Get post data
    """
    try:
        response = requests.get(params['project_url'])
    except requests.ConnectionError:
        assert False
    assert response.status_code == 200


def test_cheque_created(params):
    """
    Test cheque created
    """
    project_url = params['project_url']
    driver_remote_url = params['driver_remote_url']
    driver = webdriver.Remote(driver_remote_url, DesiredCapabilities.CHROME)
    driver.get(project_url)
    driver.find_element_by_class_name('automation-amount').send_keys('200')
    driver.find_element_by_class_name('automation-submit').click()
    page_html = driver.page_source
    driver.close()
    assert "Two Hundred" in page_html


def test_cheque_created_with_fraction_amount(params):
    """
    Test cheque created
    """
    project_url = params['project_url']
    driver_remote_url = params['driver_remote_url']
    driver = webdriver.Remote(driver_remote_url, DesiredCapabilities.CHROME)
    driver.get(project_url)
    driver.find_element_by_class_name('automation-amount').send_keys('126.23')
    driver.find_element_by_class_name('automation-submit').click()
    page_html = driver.page_source
    driver.close()
    assert "One Hundred And Twenty Six Point Two Three" in page_html
