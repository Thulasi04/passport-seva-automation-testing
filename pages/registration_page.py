from playwright.sync_api import Page
from locators import registration_locators as locate


class RegistrationPage:

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto("https://services1.passportindia.gov.in/forms/registration",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1500)

    def get_heading(self) -> str:
        heading = self.page.locator(locate.PAGE_HEADING).first
        heading.wait_for(state="visible", timeout=10000)
        return (heading.text_content() or "").strip()

    def select_office_type(self, office_type: str = "passport_office"):
        if office_type.lower() == "cpv":
            self.page.locator(locate.RADIO_CPV_DELHI).first.click()
        else:
            self.page.locator(locate.RADIO_PASSPORT_OFFICE).first.click()
        self.page.wait_for_timeout(300)

    def enter_full_name(self, full_name: str):
        input_el = self.page.locator(locate.INPUT_FULL_NAME).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(full_name)

    def get_full_name(self) -> str:
        return self.page.locator(locate.INPUT_FULL_NAME).first.input_value()

    def enter_email(self, email: str):
        input_el = self.page.locator(locate.INPUT_EMAIL).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(email)

    def get_email(self) -> str:
        return self.page.locator(locate.INPUT_EMAIL).first.input_value()

    def select_same_login_id(self, is_same: bool = True):
        if is_same:
            self.page.locator(locate.RADIO_SAME_LOGIN_ID_YES).first.click()
        else:
            self.page.locator(locate.RADIO_SAME_LOGIN_ID_NO).first.click()
        self.page.wait_for_timeout(300)

    def enter_login_id(self, login_id: str):
        input_el = self.page.locator(locate.INPUT_LOGIN_ID).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(login_id)

    def get_login_id(self) -> str:
        return self.page.locator(locate.INPUT_LOGIN_ID).first.input_value()

    def enter_password(self, password: str):
        input_el = self.page.locator(locate.INPUT_PASSWORD).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(password)

    def enter_captcha(self, captcha_text: str):
        input_el = self.page.locator(locate.INPUT_CAPTCHA).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(captcha_text)

    def click_clear(self):
        btn = self.page.locator(locate.CLEAR_BUTTON).last
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(500)

    def click_sign_up(self):
        btn = self.page.locator(locate.SIGN_UP_BUTTON).last
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(1000)

    def click_sign_in(self):
        link = self.page.locator(locate.SIGN_IN_LINK).last
        link.wait_for(state="visible", timeout=10000)
        link.click()
        self.page.wait_for_url("**/PreLogin**", timeout=10000)
