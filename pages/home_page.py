from playwright.sync_api import Page
from locators import home_locators as locate


class HomePage:

    def __init__(self, page: Page):
        self.page = page

    def open_website(self):
        """Navigate to Passport Seva homepage and wait for DOM load."""
        self.page.goto("https://www.passportindia.gov.in/psp", wait_until="domcontentloaded", timeout=30000)
        self.page.wait_for_timeout(1000)

    def get_title(self) -> str:
        """Return the document title."""
        return self.page.title().strip()

    def is_modal_visible(self) -> bool:
        """Check if the Tatkaal Advisory modal is displayed."""
        modal_btn = self.page.locator(locate.MODAL_CLOSE_BUTTON).first
        return modal_btn.is_visible(timeout=3000)

    def close_advisory_modal(self):
        """Close the Tatkaal Advisory modal if visible."""
        try:
            close_btn = self.page.locator(locate.MODAL_CLOSE_BUTTON).first
            if close_btn.is_visible(timeout=3000):
                close_btn.click()
                self.page.wait_for_timeout(500)
        except Exception:
            pass

    def open_login(self):
        """Click on the Login button in the header."""
        self.close_advisory_modal()
        login_btn = self.page.locator(locate.LOGIN_BUTTON).first
        login_btn.wait_for(state="visible", timeout=10000)
        login_btn.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_register(self):
        """Click on the Register button in the header."""
        self.close_advisory_modal()
        reg_btn = self.page.locator(locate.REGISTER_BUTTON).first
        reg_btn.wait_for(state="visible", timeout=10000)
        reg_btn.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_search_icon(self):
        """Click on the search icon to expand the search bar."""
        self.close_advisory_modal()
        search_icon = self.page.locator(locate.SEARCH_ICON).first
        search_icon.wait_for(state="visible", timeout=10000)
        search_icon.click()
        self.page.wait_for_timeout(500)

    def is_search_input_visible(self) -> bool:
        """Verify if the search input box is visible."""
        return self.page.locator(locate.SEARCH_INPUT).first.is_visible(timeout=5000)

    def enter_search_text(self, text: str):
        """Type text into the search input box."""
        self.click_search_icon()
        search_box = self.page.locator(locate.SEARCH_INPUT).first
        search_box.wait_for(state="visible", timeout=5000)
        search_box.fill(text)

    def get_search_value(self) -> str:
        """Get the current value from the search input."""
        return self.page.locator(locate.SEARCH_INPUT).first.input_value()

    def enter_pincode(self, pincode: str):
        """Enter PIN code to search nearest Passport Seva Kendra."""
        self.close_advisory_modal()
        pin_input = self.page.locator(locate.PIN_CODE_INPUT).first
        pin_input.scroll_into_view_if_needed()
        pin_input.fill(pincode)

    def get_pincode_value(self) -> str:
        """Get the entered PIN code value."""
        return self.page.locator(locate.PIN_CODE_INPUT).first.input_value()

    def click_apply_passport(self):
        """Click Quick Link: Apply For Passport."""
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_APPLY).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_check_appointment(self):
        """Click Quick Link: Check Appointment Availability."""
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_APPOINTMENT).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_track_application(self):
        """Click Quick Link: Track Passport Application."""
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_TRACK).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_register_feedback(self):
        """Click Quick Link: Register Feedback / Grievance."""
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_GRIEVANCE).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_miscellaneous_services(self):
        """Click Quick Link: Know About Our Miscellaneous Services."""
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_MISCELLANEOUS).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_ordinary_passport_service(self):
        """Click on Fresh / Re-issue Ordinary Passport card."""
        self.close_advisory_modal()
        card = self.page.locator(locate.SERVICE_ORDINARY_PASSPORT).first
        card.scroll_into_view_if_needed()
        card.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_tatkaal_service(self):
        """Click on Tatkaal Passport card."""
        self.close_advisory_modal()
        card = self.page.locator(locate.SERVICE_TATKAAL_PASSPORT).first
        card.scroll_into_view_if_needed()
        card.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_pcc_service(self):
        """Click on Police Clearance Certificate card."""
        self.close_advisory_modal()
        card = self.page.locator(locate.SERVICE_PCC).first
        card.scroll_into_view_if_needed()
        card.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_font_size(self, size_type: str = "normal"):
        """Click font resizing control: 'decrease', 'normal', or 'increase'."""
        if size_type == "decrease":
            self.page.locator(locate.FONT_DECREASE).first.click()
        elif size_type == "increase":
            self.page.locator(locate.FONT_INCREASE).first.click()
        else:
            self.page.locator(locate.FONT_NORMAL).first.click()
        self.page.wait_for_timeout(300)

    def get_call_center_text(self) -> str:
        """Retrieve national call center phone text."""
        return self.page.locator(locate.CALL_CENTER_PHONE).first.text_content() or ""

    def scroll_to_top(self):
        """Click the back to top floating button."""
        top_btn = self.page.locator(locate.SCROLL_TO_TOP_BUTTON).first
        if top_btn.is_visible(timeout=2000):
            top_btn.click()
            self.page.wait_for_timeout(500)
