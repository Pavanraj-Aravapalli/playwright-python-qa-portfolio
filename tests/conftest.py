import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def inventory_page(login_page, page):
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(page)