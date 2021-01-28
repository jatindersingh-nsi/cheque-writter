from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_just_try():
    browser = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.CHROME)
    browser.get('https://gitlab.com')
    assert 'DevOps Platform Delivered as a Single Application' in browser.title