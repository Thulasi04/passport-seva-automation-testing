from playwright.sync_api import Page
from locators import services_locators as locate


class ServicesPage:

    def __init__(self, page: Page):
        self.page = page

    def open_tatkaal_page(self):
        self.page.goto("https://www.passportindia.gov.in/psp/TatkaalPassports",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def open_fresh_passport_page(self):
        self.page.goto("https://www.passportindia.gov.in/psp/Apply",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def open_pcc_page(self):
        self.page.goto("https://www.passportindia.gov.in/psp/ApplyPCC",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def open_diplomatic_page(self):
        self.page.goto("https://www.passportindia.gov.in/psp/ApplyDiplomatic",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def open_surrender_page(self):
        self.page.goto("https://www.passportindia.gov.in/psp/ApplyIdentitySurrender",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def open_passport_act_page(self):
        self.page.goto("https://www.passportindia.gov.in/psp/PassportAct", wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def open_annexures_page(self):
        self.page.goto("https://www.passportindia.gov.in/psp/Annexures",wait_until="domcontentloaded",timeout=30000,)
        self.page.wait_for_timeout(1000)

    def get_heading(self) -> str:
        heading = self.page.locator(locate.PAGE_HEADING).first
        heading.wait_for(state="visible", timeout=10000)
        return (heading.text_content() or "").strip()
