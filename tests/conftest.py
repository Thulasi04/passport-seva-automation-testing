"""Pytest configuration and fixtures for Passport Seva UI Automation Framework.

Includes:
- Browser viewport and launch settings.
- Automatic screenshot capture on test failure.
- Integration of failure screenshots and test metadata into Pytest HTML reports.
"""

import os
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context with default desktop viewport and settings."""
    return {
        **browser_context_args,
        "viewport": {"width": 1440, "height": 900},
        "ignore_https_errors": True,
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture failure screenshots and attach them directly to Pytest HTML report."""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshots_dir = "screenshots/failures"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_name = f"{item.name}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            try:
                page.screenshot(path=file_path)
                print(f"\n[Artifact] Failure screenshot saved: {file_path}")
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html is not None:
                    extra.append(pytest_html.extras.image(file_path))
            except Exception as e:
                print(f"\n[Warning] Could not capture screenshot: {e}")

    report.extra = extra


def pytest_html_report_title(report):
    """Set custom title for generated HTML test report."""
    report.title = "Passport Seva UI Automation Test Report"


def pytest_metadata(metadata):
    """Enrich test metadata table in Pytest HTML report."""
    metadata["Project"] = "Passport Seva UI Automation Framework"
    metadata["Target Portal"] = "https://www.passportindia.gov.in"
    metadata["Design Pattern"] = "Page Object Model (POM)"
    metadata["Automation Tool"] = "Playwright (Python)"
    metadata["Author"] = "Thulasi (Passport Seva Automation)"
