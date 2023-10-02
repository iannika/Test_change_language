import pytest
from selenium.webdriver.common.by import By

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-cathedral-the-bazaar_190/"



def test_guest_should_add_to_basket(browser):
    browser.get(link)
    try: 
        button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
        button = True
    except:
        button = False  
        assert button, "button not found"

