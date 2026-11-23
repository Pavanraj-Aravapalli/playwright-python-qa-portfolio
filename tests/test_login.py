from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"


def login(page: Page, username: str, password: str):
    page.goto(BASE_URL)
    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    page.locator("#login-button").click()


def test_valid_login_shows_products_page(page: Page):
    login(page, "standard_user", "secret_sauce")
    expect(page).to_have_url(BASE_URL + "inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_locked_out_user_sees_error(page: Page):
    login(page, "locked_out_user", "secret_sauce")
    expect(page.locator("[data-test='error']")).to_contain_text("locked out")


def test_wrong_password_shows_error(page: Page):
    login(page, "standard_user", "wrong_password")
    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username and password do not match"
    )