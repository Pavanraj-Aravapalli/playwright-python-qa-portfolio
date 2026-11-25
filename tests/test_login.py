import pytest
from playwright.sync_api import expect
from pages.inventory_page import InventoryPage


def test_valid_login_shows_products_page(login_page, page):
    login_page.login("standard_user", "secret_sauce")
    inventory = InventoryPage(page)
    expect(page).to_have_url(InventoryPage.URL)
    expect(inventory.title).to_have_text("Products")


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", "secret_sauce", "locked out"),
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_login_shows_correct_error(login_page, username, password, expected_error):
    login_page.login(username, password)
    expect(login_page.error_message).to_contain_text(expected_error)