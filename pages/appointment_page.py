from playwright.sync_api import Page
from locators import appointment_locators as locate


class AppointmentPage:

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto("https://www.passportindia.gov.in/psp/checkAppointmentAvailibility",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def get_heading(self) -> str:
        heading = self.page.locator(locate.PAGE_HEADING).first
        heading.wait_for(state="visible", timeout=10000)
        return (heading.text_content() or "").strip()

    def select_passport_office(self, office_name: str):
        select_el = self.page.locator(locate.PASSPORT_OFFICE_SELECT).first
        select_el.wait_for(state="visible", timeout=10000)
        select_el.select_option(label=office_name)
        self.page.wait_for_timeout(800)

    def get_selected_office(self) -> str:
        select_el = self.page.locator(locate.PASSPORT_OFFICE_SELECT).first
        return select_el.evaluate("el => el.options[el.selectedIndex].text")

    def enter_captcha(self, captcha_text: str):
        input_el = self.page.locator(locate.CAPTCHA_INPUT).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(captcha_text)

    def get_captcha_value(self) -> str:
        return self.page.locator(locate.CAPTCHA_INPUT).first.input_value()

    def click_check_availability(self):
        btn = self.page.locator(locate.CHECK_APPOINTMENT_BUTTON).first
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(1000)

    def click_clear(self):
        clear_btn = self.page.locator(locate.CLEAR_BUTTON).first
        clear_btn.wait_for(state="visible", timeout=10000)
        clear_btn.click()
        self.page.wait_for_timeout(500)

    def is_note_for_applicants_visible(self) -> bool:
        return self.page.locator(locate.NOTE_CONTAINER).first.is_visible(timeout=5000)
