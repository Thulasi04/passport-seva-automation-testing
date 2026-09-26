import os
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot when a test fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots/failures", exist_ok=True)
            screenshot_path = (f"screenshots/failures/{item.name}.png")
            try:
                page.screenshot(path=screenshot_path)
                print(f"\nFailure screenshot saved: {screenshot_path}")
            except Exception as error:
                print(f"\nScreenshot failed: {error}")