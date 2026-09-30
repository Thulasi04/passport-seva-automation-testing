from playwright.sync_api import Page
from locators import track_status_locators as locate


class TrackStatusPage:

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto("https://www.passportindia.gov.in/psp/trackApplicationService",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def get_heading(self) -> str:
        heading = self.page.locator(locate.PAGE_HEADING).first
        heading.wait_for(state="visible", timeout=10000)
        return (heading.text_content() or "").strip()

    def select_application_type(self, app_type: str):
        select_el = self.page.locator(locate.APPLICATION_TYPE_SELECT).first
        select_el.wait_for(state="visible", timeout=10000)
        select_el.select_option(label=app_type)
        self.page.wait_for_timeout(500)

    def get_selected_application_type(self) -> str:
        select_el = self.page.locator(locate.APPLICATION_TYPE_SELECT).first
        return select_el.evaluate("el => el.options[el.selectedIndex].text")

    def enter_file_number(self, file_number: str):
        input_el = self.page.locator(locate.FILE_NUMBER_INPUT).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(file_number)

    def get_file_number(self) -> str:
        return self.page.locator(locate.FILE_NUMBER_INPUT).first.input_value()

    def enter_date_of_birth(self, dob: str):
        dob_input = self.page.locator(locate.DATE_OF_BIRTH_INPUT).first
        dob_input.wait_for(state="visible", timeout=10000)
        dob_input.fill(dob)

    def get_date_of_birth(self) -> str:
        return self.page.locator(locate.DATE_OF_BIRTH_INPUT).first.input_value()

    def click_track_status(self):
        btn = self.page.locator(locate.TRACK_STATUS_BUTTON).first
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(1000)

    def click_clear(self):
        btn = self.page.locator(locate.CLEAR_BUTTON).first
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(500)

    def is_mandatory_note_visible(self) -> bool:
        return self.page.locator(locate.MANDATORY_NOTE).first.is_visible(timeout=5000)
