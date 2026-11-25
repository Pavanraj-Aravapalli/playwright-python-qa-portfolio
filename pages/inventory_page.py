from playwright.sync_api import Page


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.items = page.locator(".inventory_item")
        self.item_prices = page.locator(".inventory_item_price")
        self.sort_dropdown = page.locator(".product_sort_container")

    def add_to_cart(self, product_name: str):
        self.items.filter(has_text=product_name).get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self, product_name: str):
        self.items.filter(has_text=product_name).get_by_role("button", name="Remove").click()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    def get_prices(self) -> list[float]:
        return [float(price.replace("$", "")) for price in self.item_prices.all_inner_texts()]