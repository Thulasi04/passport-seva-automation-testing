import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from helpers import helper_for_pages as hp


@pytest.mark.registration
def test_open_registration_page(page: Page):
    """Verify Registration page loads with expected title and heading."""
    reg = RegistrationPage(page)
    reg.open_page()
    heading = reg.get_heading()
    hp.assert_contains(heading, "User Registration")


@pytest.mark.registration
def test_select_office_type_radio(page: Page):
    """Verify selecting CPV Delhi vs Passport Office radio options."""
    reg = RegistrationPage(page)
    reg.open_page()
    reg.select_office_type("cpv")
    reg.select_office_type("passport_office")


@pytest.mark.registration
def test_fill_registration_form_fields(page: Page):
    """Verify filling registration input fields."""
    reg = RegistrationPage(page)
    reg.open_page()
    reg.enter_full_name("Rahul Sharma")
    hp.assert_contains(reg.get_full_name(), "Rahul Sharma")
    reg.enter_email("rahul.sharma.psp@example.com")
    hp.assert_page(reg.get_email().lower(),"rahul.sharma.psp@example.com")


@pytest.mark.registration
def test_clear_registration_form(page: Page):
    """Verify Clear button resets entered fields."""
    reg = RegistrationPage(page)
    reg.open_page()
    reg.enter_full_name("Anand Kumar")
    hp.assert_contains(reg.get_full_name(), "Anand Kumar")
    reg.click_clear()
    hp.assert_page(reg.get_full_name(), "")


@pytest.mark.registration
def test_navigate_to_sign_in_from_registration(page: Page):
    """Verify 'Sign In' link redirects to PreLogin page."""
    reg = RegistrationPage(page)
    reg.open_page()
    reg.click_sign_in()
    hp.assert_contains(page.url, "PreLogin")
