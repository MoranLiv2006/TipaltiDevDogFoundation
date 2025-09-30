from playwright.sync_api import Page


class DogPage:
    def __init__(self, page: Page):
        self.txt_title = page.get_by_role("heading", level="1")
