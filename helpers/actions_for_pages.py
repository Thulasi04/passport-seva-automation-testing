from playwright.sync_api import Page

def click_action(page: Page, selector: str):
    locator = page.locator(selector).first
    locator.wait_for(state="visible", timeout=10000)
    locator.click()


def type_action(page: Page, selector: str, value: str):
    locator = page.locator(selector).first
    locator.wait_for(state="visible", timeout=10000)
    locator.fill(value)


def get_text_action(page: Page, selector: str) -> str:
    locator = page.locator(selector).first
    locator.wait_for(state="visible", timeout=10000)
    return (locator.text_content() or "").strip()


def get_title_action(page: Page) -> str:
    return page.title().strip()

def select_dropdown_action(page: Page, selector: str, value_or_label: str):
    """Select option from a standard HTML select element by label or value."""
    locator = page.locator(selector).first
    locator.wait_for(state="visible", timeout=10000)
    try:
        locator.select_option(label=value_or_label)
    except Exception:
        locator.select_option(value=value_or_label)


def is_visible_action(page: Page, selector: str, timeout: int = 5000) -> bool:
    try:
        locator = page.locator(selector).first
        return locator.is_visible(timeout=timeout)
    except Exception:
        return False


def get_input_value_action(page: Page, selector: str) -> str:
    locator = page.locator(selector).first
    locator.wait_for(state="attached", timeout=10000)
    return locator.input_value()


def clear_input_action(page: Page, selector: str):
    locator = page.locator(selector).first
    locator.wait_for(state="visible", timeout=10000)
    locator.fill("")
