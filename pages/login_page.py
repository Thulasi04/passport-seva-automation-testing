from playwright.sync_api import Page
from locators import login_locators as locate


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto("https://services1.passportindia.gov.in/forms/PreLogin",wait_until="domcontentloaded",timeout=30000, )
        self.page.wait_for_timeout(1500)

    def get_heading(self) -> str:
        heading = self.page.locator(locate.PAGE_HEADING).first
        heading.wait_for(state="visible", timeout=10000)
        return (heading.text_content() or "").strip()

    def enter_login_id(self, login_id: str):
        input_el = self.page.locator(locate.LOGIN_ID_INPUT).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(login_id)

    def get_login_id_value(self) -> str:
        return self.page.locator(locate.LOGIN_ID_INPUT).first.input_value()

    def click_continue(self):
        btn = self.page.locator(locate.CONTINUE_BUTTON).first
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(1000)

    def click_register_here(self):
        link = self.page.locator(locate.REGISTER_HERE_LINK).first
        link.wait_for(state="visible", timeout=10000)
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_trouble_logging_in(self):
        link = self.page.locator(locate.TROUBLE_LOGGING_IN_LINK).first
        link.wait_for(state="visible", timeout=10000)
        link.click()

    def is_attention_notice_visible(self) -> bool:
        return self.page.locator(locate.ATTENTION_NOTICE).first.is_visible(timeout=5000)
