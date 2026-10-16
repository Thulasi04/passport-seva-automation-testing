import os
from playwright.sync_api import Page, expect

DEFAULT_BASE_URL = "https://www.passportindia.gov.in/psp"

def open_website(page: Page, url: str = DEFAULT_BASE_URL):
    page.goto(url, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(1000)

def dismiss_advisory_modal(page: Page):
    try:
        close_btn = page.locator(".homePageModal button.btn-close, button.btn-close, [aria-label='Close'], button:has-text('✕')").first
        if close_btn.is_visible(timeout=1500):
            close_btn.click(force=True)
            page.wait_for_timeout(300)
        page.evaluate("""() => {
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


def assert_page(actual, expected):
    assert actual == expected, f"Assertion failed: Expected '{expected}', but got '{actual}'"

def assert_contains(actual: str, expected: str):
    assert expected.lower() in actual.lower(), (
        f"Assertion failed: Expected '{expected}' to be contained in '{actual}'"
    )

def assert_visible(page: Page, selector: str, timeout: int = 5000):
    locator = page.locator(selector).first
    expect(locator).to_be_visible(timeout=timeout)


def take_screenshot(
    page: Page,
    name: str,
    status: str = "passed",
    directory: str = "reports",
) -> str:
    """Capture a screenshot and store it directly in reports/passed/ or reports/failed/."""
    target_dir = os.path.join(directory, status)
    os.makedirs(target_dir, exist_ok=True)
    file_path = os.path.join(target_dir, f"{name}.png")
    page.screenshot(path=file_path, full_page=False)
    return file_path


