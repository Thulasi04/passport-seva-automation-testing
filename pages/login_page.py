from playwright.sync_api import Page
from locators import login_locators as locate


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        """Navigate directly to the PreLogin page."""
        self.page.goto("https://services1.passportindia.gov.in/forms/PreLogin",wait_until="domcontentloaded",timeout=30000, )
        self.page.wait_for_timeout(1500)

    def get_heading(self) -> str:
        """Get the Login header title."""
        heading = self.page.locator(locate.PAGE_HEADING).first
        heading.wait_for(state="visible", timeout=10000)
        return (heading.text_content() or "").strip()

    def enter_login_id(self, login_id: str):
        """Enter user Login ID into the outlined text input."""
        input_el = self.page.locator(locate.LOGIN_ID_INPUT).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(login_id)

    def get_login_id_value(self) -> str:
        """Get current value in Login ID field."""
        return self.page.locator(locate.LOGIN_ID_INPUT).first.input_value()

    def click_continue(self):
        """Click on the Continue button."""
        btn = self.page.locator(locate.CONTINUE_BUTTON).first
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(1000)

    def click_register_here(self):
        """Click the 'Register here' link."""
        link = self.page.locator(locate.REGISTER_HERE_LINK).first
        link.wait_for(state="visible", timeout=10000)
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_trouble_logging_in(self):
        """Click 'Having Trouble Logging in ?' link."""
        link = self.page.locator(locate.TROUBLE_LOGGING_IN_LINK).first
        link.wait_for(state="visible", timeout=10000)
        link.click()

    def is_attention_notice_visible(self) -> bool:
        """Verify visibility of the Attention Notice."""
        return self.page.locator(locate.ATTENTION_NOTICE).first.is_visible(timeout=5000)
