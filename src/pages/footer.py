from playwright.sync_api import Page


class Footer:
    def __init__(self, page: Page):
        self.input_name = page.locator("#name")
        self.input_email = page.locator("#email")
        self.input_message = page.locator("#message")
        self.btn_send = page.get_by_role("button", name="Send")
