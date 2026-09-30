import pytest
from playwright.sync_api import Page
from pages.track_status_page import TrackStatusPage
from helpers import helper_for_pages as hp


@pytest.mark.tracking
def test_open_track_status_page(page: Page):
    track = TrackStatusPage(page)
    track.open_page()
    heading = track.get_heading()
    hp.assert_contains(heading, "Track Application Status")


@pytest.mark.tracking
def test_select_application_type_passport(page: Page):
    track = TrackStatusPage(page)
    track.open_page()
    track.select_application_type("Passport/PCC/IC/GEP")
    selected = track.get_selected_application_type()
    hp.assert_contains(selected, "PASSPORT")


@pytest.mark.tracking
def test_enter_file_number(page: Page):
    track = TrackStatusPage(page)
    track.open_page()
    track.enter_file_number("CHN074589632124")
    file_no = track.get_file_number()
    hp.assert_page(file_no, "CHN074589632124")


@pytest.mark.tracking
def test_enter_date_of_birth(page: Page):
    track = TrackStatusPage(page)
    track.open_page()
    track.enter_date_of_birth("1995-08-15")
    dob = track.get_date_of_birth()
    hp.assert_page(dob, "1995-08-15")


@pytest.mark.tracking
def test_clear_tracking_form(page: Page):
    track = TrackStatusPage(page)
    track.open_page()
    track.enter_file_number("CHN123456789012")
    hp.assert_page(track.get_file_number(), "CHN123456789012")
    track.click_clear()
    hp.assert_page(track.get_file_number(), "")
