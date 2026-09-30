import pytest
from playwright.sync_api import Page
from pages.services_page import ServicesPage
from helpers import helper_for_pages as hp


@pytest.mark.services
def test_open_tatkaal_service_page(page: Page):
    service = ServicesPage(page)
    service.open_tatkaal_page()
    heading = service.get_heading()
    hp.assert_contains(heading, "Tatkaal")


@pytest.mark.services
def test_open_fresh_passport_page(page: Page):
    service = ServicesPage(page)
    service.open_fresh_passport_page()
    hp.assert_contains(page.url, "Apply")


@pytest.mark.services
def test_open_pcc_service_page(page: Page):
    service = ServicesPage(page)
    service.open_pcc_page()
    hp.assert_contains(page.url, "ApplyPCC")


@pytest.mark.services
def test_open_diplomatic_passport_page(page: Page):
    service = ServicesPage(page)
    service.open_diplomatic_page()
    hp.assert_contains(page.url, "ApplyDiplomatic")


@pytest.mark.services
def test_open_surrender_certificate_page(page: Page):
    service = ServicesPage(page)
    service.open_surrender_page()
    hp.assert_contains(page.url, "ApplyIdentitySurrender")


@pytest.mark.services
def test_open_passport_act_rules_page(page: Page):
    service = ServicesPage(page)
    service.open_passport_act_page()
    hp.assert_contains(page.url, "PassportAct")
