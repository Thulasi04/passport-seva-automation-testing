import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from helpers import helper_for_pages as hp


@pytest.mark.login
def test_open_login_page(page: Page):
    login = LoginPage(page)
    login.open_page()
    heading = login.get_heading()
    hp.assert_contains(heading, "Login")


@pytest.mark.login
def test_login_attention_notice_displayed(page: Page):
    login = LoginPage(page)
    login.open_page()
    is_visible = login.is_attention_notice_visible()
    hp.assert_page(is_visible, True)


@pytest.mark.login
def test_enter_login_id_input(page: Page):
    login = LoginPage(page)
    login.open_page()
    login.enter_login_id("testuser_psp2026")
    val = login.get_login_id_value()
    hp.assert_contains(val, "testuser_psp2026")


@pytest.mark.login
def test_navigate_to_register_from_login(page: Page):
    login = LoginPage(page)
    login.open_page()
    login.click_register_here()
    hp.assert_contains(page.url, "registration")
