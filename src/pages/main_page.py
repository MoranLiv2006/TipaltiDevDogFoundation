from playwright.sync_api import Page, Locator


class MainPage:
    def __init__(self, page: Page):
        self.btn_hamburger = page.get_by_role("link", name="Menu")
        self.list_tiles = page.locator("section[class='tiles'] > article > a > h2")
