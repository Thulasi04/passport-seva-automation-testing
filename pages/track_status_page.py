from playwright.sync_api import Page
from locators import track_status_locators as locate


class TrackStatusPage:

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        """Navigate directly to Track Passport Application page."""
        self.page.goto("https://www.passportindia.gov.in/psp/trackApplicationService",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def get_heading(self) -> str:
        """Get the page heading text."""
        heading = self.page.locator(locate.PAGE_HEADING).first
        heading.wait_for(state="visible", timeout=10000)
        return (heading.text_content() or "").strip()

    def select_application_type(self, app_type: str):
        """Select an Application Type from the dropdown."""
        select_el = self.page.locator(locate.APPLICATION_TYPE_SELECT).first
        select_el.wait_for(state="visible", timeout=10000)
        select_el.select_option(label=app_type)
        self.page.wait_for_timeout(500)

    def get_selected_application_type(self) -> str:
        """Get the currently selected Application Type display text."""
        select_el = self.page.locator(locate.APPLICATION_TYPE_SELECT).first
        return select_el.evaluate("el => el.options[el.selectedIndex].text")

    def enter_file_number(self, file_number: str):
        """Enter the Passport Application File Number."""
        input_el = self.page.locator(locate.FILE_NUMBER_INPUT).first
        input_el.wait_for(state="visible", timeout=10000)
        input_el.fill(file_number)

    def get_file_number(self) -> str:
        """Get the entered File Number."""
        return self.page.locator(locate.FILE_NUMBER_INPUT).first.input_value()

    def enter_date_of_birth(self, dob: str):
        """Enter Date of Birth in YYYY-MM-DD or DD/MM/YYYY format."""
        dob_input = self.page.locator(locate.DATE_OF_BIRTH_INPUT).first
        dob_input.wait_for(state="visible", timeout=10000)
        dob_input.fill(dob)

    def get_date_of_birth(self) -> str:
        """Get the entered Date of Birth value."""
        return self.page.locator(locate.DATE_OF_BIRTH_INPUT).first.input_value()

    def click_track_status(self):
        """Click on the Track Application Status button."""
        btn = self.page.locator(locate.TRACK_STATUS_BUTTON).first
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(1000)

    def click_clear(self):
        """Click on the Clear button to reset the tracking form."""
        btn = self.page.locator(locate.CLEAR_BUTTON).first
        btn.wait_for(state="visible", timeout=10000)
        btn.click()
        self.page.wait_for_timeout(500)

    def is_mandatory_note_visible(self) -> bool:
        """Verify visibility of the mandatory fields indicator."""
        return self.page.locator(locate.MANDATORY_NOTE).first.is_visible(timeout=5000)
