import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from helpers import helper_for_pages as hp


@pytest.mark.home
def test_open_passport_seva_home(page: Page):
    home = HomePage(page)
    home.open_website()
    title = home.get_title()
    hp.assert_contains(title, "Passport Seva")


@pytest.mark.home
def test_advisory_modal_dismissal(page: Page):
    home = HomePage(page)
    home.open_website()
    if home.is_modal_visible():
        home.close_advisory_modal()
        hp.assert_page(home.is_modal_visible(), False)


@pytest.mark.home
def test_national_call_center_info(page: Page):
    home = HomePage(page)
    home.open_website()
    call_center_text = home.get_call_center_text()
    hp.assert_contains(call_center_text, "1800-258-1800")


@pytest.mark.home
def test_search_bar_expansion_and_input(page: Page):
    home = HomePage(page)
    home.open_website()
    home.enter_search_text("Tatkaal")
    val = home.get_search_value()
    hp.assert_page(val, "Tatkaal")


@pytest.mark.home
def test_pincode_locator_input(page: Page):
    home = HomePage(page)
    home.open_website()
    home.enter_pincode("600001")
    val = home.get_pincode_value()
    hp.assert_page(val, "600001")


@pytest.mark.navigation
def test_quick_link_check_appointment(page: Page):
    home = HomePage(page)
    home.open_website()
    home.click_check_appointment()
    hp.assert_contains(page.url, "checkAppointmentAvailibility")


@pytest.mark.navigation
def test_quick_link_track_application(page: Page):
    home = HomePage(page)
    home.open_website()
    home.click_track_application()
    hp.assert_contains(page.url, "trackApplicationService")


@pytest.mark.navigation
def test_quick_link_apply_passport(page: Page):
    home = HomePage(page)
    home.open_website()
    home.click_apply_passport()
    hp.assert_contains(page.url, "ApplyPassport")


@pytest.mark.accessibility
def test_accessibility_font_resizing(page: Page):
    home = HomePage(page)
    home.open_website()
    home.close_advisory_modal()
    home.click_font_size("increase")
    home.click_font_size("normal")
    home.click_font_size("decrease")
