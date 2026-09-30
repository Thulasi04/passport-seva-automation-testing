import pytest
from playwright.sync_api import Page
from pages.appointment_page import AppointmentPage
from helpers import helper_for_pages as hp


@pytest.mark.appointment
def test_open_appointment_availability_page(page: Page):
    apt = AppointmentPage(page)
    apt.open_page()
    heading = apt.get_heading()
    hp.assert_contains(heading, "Check Appointment Availability")


@pytest.mark.appointment
def test_select_passport_office_dropdown(page: Page):
    apt = AppointmentPage(page)
    apt.open_page()
    apt.select_passport_office("Chennai")
    selected = apt.get_selected_office()
    hp.assert_contains(selected, "Chennai")


@pytest.mark.appointment
def test_enter_captcha_input(page: Page):
    apt = AppointmentPage(page)
    apt.open_page()
    apt.enter_captcha("AB12CD")
    val = apt.get_captcha_value()
    hp.assert_page(val, "AB12CD")


@pytest.mark.appointment
def test_clear_appointment_form(page: Page):
    apt = AppointmentPage(page)
    apt.open_page()
    apt.enter_captcha("TEST1234")
    hp.assert_page(apt.get_captcha_value(), "TEST1234")
    apt.click_clear()
    hp.assert_page(apt.get_captcha_value(), "")


@pytest.mark.appointment
def test_applicants_note_visibility(page: Page):
    apt = AppointmentPage(page)
    apt.open_page()
    is_visible = apt.is_note_for_applicants_visible()
    hp.assert_page(is_visible, True)
