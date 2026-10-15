"""Pytest configuration and fixtures for Passport Seva UI Automation Framework.

Includes:
- Browser viewport and launch settings.
- Automatic screenshot capture on test completion (categorized into 'passed' and 'failed' folders).
- Direct embedding of screenshots into self-contained Pytest HTML reports.
- Custom metadata formatting for enterprise test reporting.
"""

import os
import shutil
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context with desktop viewport and security bypass."""
    return {
        **browser_context_args,
        "viewport": {"width": 1440, "height": 900},
        "ignore_https_errors": True,
    }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshots for passed and failed tests into structured folders and attach to HTML report."""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        page = item.funcargs.get("page")
        if page:
            status = "failed" if report.failed else "passed"
            file_name = f"{item.name}.png"

            # Primary directories for reports and standalone screenshot archives
            reports_screenshot_dir = os.path.join("reports", "screenshots", status)
            root_screenshot_dir = os.path.join("screenshots", status)

            os.makedirs(reports_screenshot_dir, exist_ok=True)
            os.makedirs(root_screenshot_dir, exist_ok=True)

            report_file_path = os.path.join(reports_screenshot_dir, file_name)
            root_file_path = os.path.join(root_screenshot_dir, file_name)

            try:
                page.screenshot(path=report_file_path)
                # Sync screenshot to screenshots/{status}/ as well
                try:
                    shutil.copyfile(report_file_path, root_file_path)
                except Exception:
                    pass

                print(f"\n[Screenshot] Saved {status.upper()} screenshot -> {report_file_path}")

                # Attach image to Pytest HTML report
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html is not None:
                    extra.append(pytest_html.extras.image(report_file_path, f"{status.capitalize()}: {item.name}"))
            except Exception as e:
                print(f"\n[Warning] Could not capture {status} screenshot: {e}")

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
    metadata["Screenshot Storage"] = "reports/screenshots/ (passed & failed)"
