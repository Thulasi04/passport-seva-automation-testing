import os
from playwright.sync_api import Page, expect

DEFAULT_BASE_URL = "https://www.passportindia.gov.in/psp"


def open_website(page: Page, url: str = DEFAULT_BASE_URL):
    """Navigate to the target URL and wait for DOM content to load."""
    page.goto(url, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(1000)


def dismiss_advisory_modal(page: Page):
    """Dismiss the initial Tatkaal Advisory modal if it is displayed."""
    try:
        close_btn = page.locator("button:has-text('✕'), button.btn-close, .modal button").first
        if close_btn.is_visible(timeout=3000):
            close_btn.click()
            page.wait_for_timeout(500)
    except Exception:
        pass


def assert_page(actual, expected):
    """Assert exact equality between actual and expected values."""
    assert actual == expected, f"Assertion failed: Expected '{expected}', but got '{actual}'"


def assert_contains(actual: str, expected: str):
    """Assert substring presence (case-insensitive)."""
    assert expected.lower() in actual.lower(), (
        f"Assertion failed: Expected '{expected}' to be contained in '{actual}'"
    )


def assert_visible(page: Page, selector: str, timeout: int = 5000):
    """Assert that the element matching the selector is visible."""
    locator = page.locator(selector).first
    expect(locator).to_be_visible(timeout=timeout)


def take_screenshot(page: Page, name: str, directory: str = "screenshots"):
    """Capture a screenshot and save to the specified directory."""
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f"{name}.png")
    page.screenshot(path=file_path, full_page=False)
    return file_path
