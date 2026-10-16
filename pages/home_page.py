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
            if close_btn.is_visible(timeout=1500):
                close_btn.click(force=True)
                self.page.wait_for_timeout(300)
            self.page.evaluate("""() => {
                document.querySelectorAll('.modal-backdrop, .modal, .homePageModal').forEach(el => {
                    if (el) {
                        el.classList.remove('show');
                        el.style.display = 'none';
                        el.style.pointerEvents = 'none';
                    }
                });
                if (!document.getElementById('suppress-modals-style')) {
                    const style = document.createElement('style');
                    style.id = 'suppress-modals-style';
                    style.innerHTML = '.modal-backdrop, .homePageModal, .modal.show { display: none !important; pointer-events: none !important; }';
                    document.head.appendChild(style);
                }
            }""")
        except Exception:
            pass

    def _safe_click(self, selector: str, timeout: int = 5000):
        self.close_advisory_modal()
        locator = self.page.locator(selector).first
        locator.scroll_into_view_if_needed()
        try:
            locator.click(timeout=timeout)
        except Exception:
            self.close_advisory_modal()
            locator.click(force=True)
        self.page.wait_for_load_state("domcontentloaded")

    def open_login(self):
        self._safe_click(locate.LOGIN_BUTTON)

    def open_register(self):
        self._safe_click(locate.REGISTER_BUTTON)

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
        self._safe_click(locate.QUICK_LINK_APPLY)

    def click_check_appointment(self):
        self._safe_click(locate.QUICK_LINK_APPOINTMENT)

    def click_track_application(self):
        self._safe_click(locate.QUICK_LINK_TRACK)

    def click_register_feedback(self):
        self._safe_click(locate.QUICK_LINK_GRIEVANCE)

    def click_miscellaneous_services(self):
        self._safe_click(locate.QUICK_LINK_MISCELLANEOUS)

    def click_ordinary_passport_service(self):
        self._safe_click(locate.SERVICE_ORDINARY_PASSPORT)

    def click_tatkaal_service(self):
        self._safe_click(locate.SERVICE_TATKAAL_PASSPORT)

    def click_pcc_service(self):
        self._safe_click(locate.SERVICE_PCC)

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
