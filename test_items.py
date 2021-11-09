import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_cart_on_page(browser):
    browser.get(link)
    button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert button, "No button on this page"
    