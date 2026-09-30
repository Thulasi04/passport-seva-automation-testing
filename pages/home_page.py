from playwright.sync_api import Page
from locators import home_locators as locate


class HomePage:

    def __init__(self, page: Page):
        self.page = page

    def open_website(self):
        self.page.goto("https://www.passportindia.gov.in/psp", wait_until="domcontentloaded", timeout=30000)
        self.page.wait_for_timeout(1000)

    def get_title(self) -> str:
        return self.page.title().strip()

    def is_modal_visible(self) -> bool:
        modal_btn = self.page.locator(locate.MODAL_CLOSE_BUTTON).first
        return modal_btn.is_visible(timeout=3000)

    def close_advisory_modal(self):
        try:
            close_btn = self.page.locator(locate.MODAL_CLOSE_BUTTON).first
            if close_btn.is_visible(timeout=3000):
                close_btn.click()
                self.page.wait_for_timeout(500)
        except Exception:
            pass

    def open_login(self):
        self.close_advisory_modal()
        login_btn = self.page.locator(locate.LOGIN_BUTTON).first
        login_btn.wait_for(state="visible", timeout=10000)
        login_btn.click()
        self.page.wait_for_load_state("domcontentloaded")

    def open_register(self):
        self.close_advisory_modal()
        reg_btn = self.page.locator(locate.REGISTER_BUTTON).first
        reg_btn.wait_for(state="visible", timeout=10000)
        reg_btn.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_search_icon(self):
        self.close_advisory_modal()
        search_icon = self.page.locator(locate.SEARCH_ICON).first
        search_icon.wait_for(state="visible", timeout=10000)
        search_icon.click()
        self.page.wait_for_timeout(500)

    def is_search_input_visible(self) -> bool:
        return self.page.locator(locate.SEARCH_INPUT).first.is_visible(timeout=5000)

    def enter_search_text(self, text: str):
        self.click_search_icon()
        search_box = self.page.locator(locate.SEARCH_INPUT).first
        search_box.wait_for(state="visible", timeout=5000)
        search_box.fill(text)

    def get_search_value(self) -> str:
        return self.page.locator(locate.SEARCH_INPUT).first.input_value()

    def enter_pincode(self, pincode: str):
        self.close_advisory_modal()
        pin_input = self.page.locator(locate.PIN_CODE_INPUT).first
        pin_input.scroll_into_view_if_needed()
        pin_input.fill(pincode)

    def get_pincode_value(self) -> str:
        return self.page.locator(locate.PIN_CODE_INPUT).first.input_value()

    def click_apply_passport(self):
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_APPLY).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_check_appointment(self):
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_APPOINTMENT).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_track_application(self):
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_TRACK).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_register_feedback(self):
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_GRIEVANCE).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_miscellaneous_services(self):
        self.close_advisory_modal()
        link = self.page.locator(locate.QUICK_LINK_MISCELLANEOUS).first
        link.scroll_into_view_if_needed()
        link.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_ordinary_passport_service(self):
        self.close_advisory_modal()
        card = self.page.locator(locate.SERVICE_ORDINARY_PASSPORT).first
        card.scroll_into_view_if_needed()
        card.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_tatkaal_service(self):
        self.close_advisory_modal()
        card = self.page.locator(locate.SERVICE_TATKAAL_PASSPORT).first
        card.scroll_into_view_if_needed()
        card.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_pcc_service(self):
        self.close_advisory_modal()
        card = self.page.locator(locate.SERVICE_PCC).first
        card.scroll_into_view_if_needed()
        card.click()
        self.page.wait_for_load_state("domcontentloaded")

    def click_font_size(self, size_type: str = "normal"):
        if size_type == "decrease":
            self.page.locator(locate.FONT_DECREASE).first.click()
        elif size_type == "increase":
            self.page.locator(locate.FONT_INCREASE).first.click()
        else:
            self.page.locator(locate.FONT_NORMAL).first.click()
        self.page.wait_for_timeout(300)

    def get_call_center_text(self) -> str:
        return self.page.locator(locate.CALL_CENTER_PHONE).first.text_content() or ""

    def scroll_to_top(self):
        top_btn = self.page.locator(locate.SCROLL_TO_TOP_BUTTON).first
        if top_btn.is_visible(timeout=2000):
            top_btn.click()
            self.page.wait_for_timeout(500)
