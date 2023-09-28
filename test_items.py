import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_add_to_basket(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")  
   