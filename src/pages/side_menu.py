from playwright.sync_api import Page


class SideMenu:
    def __init__(self, page: Page):
        self.txt_title = page.get_by_role("heading", level=2)
        self.list_menu_items = page.locator("div[class='inner'] > ul > li")