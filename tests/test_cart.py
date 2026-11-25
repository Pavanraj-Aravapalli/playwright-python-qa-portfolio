from playwright.sync_api import expect


def test_add_item_updates_cart_badge(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")


def test_remove_item_clears_cart_badge(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.remove_from_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_be_hidden()


def test_sort_by_price_low_to_high(inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.get_prices()
    assert prices == sorted(prices)