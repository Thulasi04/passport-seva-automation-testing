# 🛂 Passport Seva UI Automation Testing Framework

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-8.0%2B-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Page_Object_Model_(POM)-F7931E?style=for-the-badge)](https://martinfowler.com/bliki/PageObject.html)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/Thulasi04/passport-seva-automation-testing/actions)
[![Test Suite](https://img.shields.io/badge/Tests-34%20Passed-brightgreen?style=for-the-badge)](#test-suite-breakdown)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

An enterprise-grade, end-to-end UI automation testing framework built for the official **[Passport Seva Portal](https://www.passportindia.gov.in/psp)** (Ministry of External Affairs, Government of India). 

Developed with **Python**, **Playwright**, and **Pytest**, this framework implements industry-standard **Page Object Model (POM)** architecture, resilient synchronization strategies, comprehensive test reporting with failure screenshots, and a fully automated **GitHub Actions CI/CD pipeline**.

---

## 📌 Table of Contents

- [Key Highlights](#-key-highlights)
- [Framework Architecture](#-framework-architecture)
- [Project Structure](#-project-structure)
- [Test Suite Breakdown](#-test-suite-breakdown)
- [Getting Started](#-getting-started)
- [Executing Tests](#-executing-tests)
- [Reporting & Diagnostics](#-reporting--diagnostics)
- [Continuous Integration (CI/CD)](#-continuous-integration-cicd)
- [Engineering Best Practices](#-engineering-best-practices)
- [Author & Acknowledgments](#-author--acknowledgments)

---

## ✨ Key Highlights

- **Page Object Model (POM)**: Strict decoupling of page element locators, page actions, and test assertions for maximum maintainability and test reusability.
- **Robust Synchronization & Modal Handling**: Intelligent handling of transient modal overlays (e.g. *Tatkaal Advisory* dialogs and backdrop fades) using Playwright's dynamic waiting mechanism and DOM cleanup fallbacks to prevent flaky tests.
- **Comprehensive Coverage (34 Automated Tests)**: Verifies critical user flows including home navigation, appointment availability dropdowns, application tracking, user registration, PreLogin flows, and statutory service catalogs.
- **Automated Failure Screenshots**: Built-in Pytest hooks automatically capture full-resolution screenshots upon any test failure and embed them directly into self-contained HTML reports.
- **Parallel Test Execution**: Built-in support for `pytest-xdist` to execute test suites concurrently across multiple worker processes, drastically reducing test execution time.
- **GitHub Actions CI/CD Pipeline**: Automated test runs on every pull request and push to `main`, archiving HTML test reports and artifacts for team inspection.

---

## 🏗 Framework Architecture

The framework adheres to the **Page Object Model (POM)** design pattern:

```
┌────────────────────────────────────────────────────────┐
│                   Test Layer (Pytest)                  │
│   tests/test_home.py       tests/test_appointment.py   │
│   tests/test_login.py      tests/test_registration.py  │
│   tests/test_services.py   tests/test_track_status.py  │
└───────────────────────────┬────────────────────────────┘
                            │ Calls Page Actions
┌───────────────────────────▼────────────────────────────┐
│                    Page Objects Layer                  │
│   HomePage                 AppointmentPage             │
│   LoginPage                RegistrationPage            │
│   ServicesPage             TrackStatusPage             │
└─────────────┬───────────────────────────┬──────────────┘
              │ Uses                      │ Executes
┌─────────────▼─────────────┐ ┌───────────▼──────────────┐
│       Locators Layer      │ │       Helpers Layer      │
│   Centralized Selectors   │ │   Action Primitives &    │
│   CSS / Text / Roles      │ │   Custom Assertions      │
└───────────────────────────┘ └──────────────────────────┘
```

---

## 📂 Project Structure

```bash
passport-seva-automation-testing/
├── .github/
│   └── workflows/
│       └── playwright.yml         # GitHub Actions CI/CD pipeline
├── helpers/
│   ├── __init__.py
│   ├── actions_for_pages.py       # Reusable element actions (type, click, select)
│   └── helper_for_pages.py        # Assertion helpers, modal dismissal, navigation
├── locators/
│   ├── __init__.py
│   ├── appointment_locators.py    # Appointment availability element selectors
│   ├── home_locators.py           # Homepage, modal, navbar & quick link selectors
│   ├── login_locators.py          # User authentication selectors
│   ├── registration_locators.py   # Citizen registration form selectors
│   ├── services_locators.py       # Passport service catalog selectors
│   └── track_status_locators.py   # Application status tracking selectors
├── pages/
│   ├── __init__.py                # Package-level page exports
│   ├── appointment_page.py        # Appointment booking & availability page actions
│   ├── home_page.py               # Homepage actions & modal handling
│   ├── login_page.py              # Login page interactions
│   ├── registration_page.py       # Registration workflow interactions
│   ├── services_page.py           # Services catalog interactions
│   └── track_status_page.py       # Status tracking form interactions
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures, failure screenshots & report hooks
│   ├── test_appointment.py       # Appointment availability tests (5 tests)
│   ├── test_home.py              # Home layout & navigation tests (9 tests)
│   ├── test_login.py             # Login & PreLogin flow tests (4 tests)
│   ├── test_registration.py      # User registration tests (5 tests)
│   ├── test_services.py          # Passport services catalog tests (6 tests)
│   └── test_track_status.py      # Status tracking tests (5 tests)
├── .gitignore                     # Git ignore rules for Python, cache & reports
├── pytest.ini                     # Pytest configuration, registered markers & flags
├── requirements.txt               # Pinned dependencies
└── README.md                      # Framework documentation
```

---

## 🧪 Test Suite Breakdown

The test suite covers **34 end-to-end scenarios** across 6 core functional modules:

| Test Module | Marker | Test Count | Scope & Coverage |
| :--- | :--- | :---: | :--- |
| [`test_home.py`](file:///Users/udayakumar/Desktop/passportseva/tests/test_home.py) | `@pytest.mark.home`<br>`@pytest.mark.navigation`<br>`@pytest.mark.accessibility` | **9** | Homepage loading, branding validation, advisory modal dismissal, national call center info (1800-258-1800), search bar expansion, PIN code locator input, accessibility font resizing (A+, A, A-), quick navigation links (Check Appointment, Track Application, Apply Passport). |
| [`test_login.py`](file:///Users/udayakumar/Desktop/passportseva/tests/test_login.py) | `@pytest.mark.login` | **4** | PreLogin page navigation, attention notices visibility, Login ID input interaction and data verification, navigation to citizen registration. |
| [`test_registration.py`](file:///Users/udayakumar/Desktop/passportseva/tests/test_registration.py) | `@pytest.mark.registration` | **5** | User registration page heading, office type radio toggle (CPV Delhi vs Passport Office), multi-field form population (Full Name, Email), form clear reset validation, navigation back to sign in. |
| [`test_appointment.py`](file:///Users/udayakumar/Desktop/passportseva/tests/test_appointment.py) | `@pytest.mark.appointment` | **5** | Appointment availability header verification, Passport Office selection dropdown (e.g. Chennai), Captcha entry field, reset form action, and "Note for Applicants" visibility check. |
| [`test_services.py`](file:///Users/udayakumar/Desktop/passportseva/tests/test_services.py) | `@pytest.mark.services` | **6** | Service catalogs verification: Tatkaal Passport scheme, Fresh/Re-issue Ordinary Passport, Police Clearance Certificate (PCC), Diplomatic/Official Passport, Surrender Certificate, and Passports Act & Rules. |
| [`test_track_status.py`](file:///Users/udayakumar/Desktop/passportseva/tests/test_track_status.py) | `@pytest.mark.tracking` | **5** | Application tracking page heading, Application Type dropdown (`Passport/PCC/IC/GEP`), file number input, Date of Birth picker interaction, and form reset. |

**Total Test Count: 34 Tests (100% Passing)**

---

## 🚀 Getting Started

### Prerequisites

- **Python**: Version 3.10, 3.11, 3.12, or higher
- **Git**: Installed and configured
- **Virtual Environment Tool**: `venv` or `conda`

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Thulasi04/passport-seva-automation-testing.git
   cd passport-seva-automation-testing
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # On macOS/Linux:
   python3 -m venv .venv
   source .venv/bin/activate

   # On Windows (CMD/PowerShell):
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Install Playwright browser binaries**:
   ```bash
   playwright install --with-deps chromium
   ```

---

## 🏃 Executing Tests

### 1. Run the entire test suite
```bash
pytest
```
*(Automatically generates a self-contained HTML report in `reports/report.html`)*

### 2. Run specific test modules
```bash
# Run homepage tests
pytest tests/test_home.py

# Run appointment availability tests
pytest tests/test_appointment.py

# Run registration tests
pytest tests/test_registration.py
```

### 3. Run by Pytest markers
```bash
# Run only login tests
pytest -m login

# Run only appointment tests
pytest -m appointment

# Run only tracking tests
pytest -m tracking

# Run services tests
pytest -m services
```

### 4. Run tests with visual browser UI (Headed Mode)
```bash
pytest --headed --slowmo 500
```

### 5. Run tests in parallel (Speed Optimization)
```bash
pytest -n auto
```

---

## 📊 Reporting & Diagnostics

### Self-Contained HTML Reports
The framework uses `pytest-html` to produce standalone test reports containing execution status, run duration, environment metadata, and stack traces.

Generate an on-demand report:
```bash
pytest --html=reports/report.html --self-contained-html
```

### Automated Failure Screenshots
Configured inside [`tests/conftest.py`](file:///Users/udayakumar/Desktop/passportseva/tests/conftest.py), whenever an assertion fails during test execution:
1. Playwright immediately takes a full browser screenshot.
2. The image is saved to `screenshots/failures/<test_name>.png`.
3. The screenshot is automatically embedded directly into the HTML test report for rapid debugging.

---

## 🔄 Continuous Integration (CI/CD)

The repository features an automated GitHub Actions workflow defined in [`.github/workflows/playwright.yml`](file:///Users/udayakumar/Desktop/passportseva/.github/workflows/playwright.yml).

### Pipeline Workflow:
1. **Trigger**: Activated on every `push` to `main` and on all `pull_request` events.
2. **Setup**: Provisions an Ubuntu runner, configures Python 3.12, and caches pip dependencies.
3. **Install**: Installs framework requirements and downloads Chromium browser binaries.
4. **Execution**: Runs the entire test suite with Pytest in headless mode.
5. **Artifact Publishing**:
   - Always uploads the self-contained `reports/report.html` as a workflow artifact.
   - Automatically archives any failure screenshots if any test fails.

---

## 💡 Engineering Best Practices

- **Explicit Separation of Concerns**: Test logic contains zero locator definitions or raw browser interactions; all interactions flow through Page Objects.
- **Zero Hardcoded Sleeps**: Relies on Playwright's auto-wait mechanisms and explicit DOM state expectations rather than arbitrary delays.
- **Clean Configuration**: Uses [`pytest.ini`](file:///Users/udayakumar/Desktop/passportseva/pytest.ini) to eliminate unknown marker warnings and enforce consistent CLI parameters.
- **Fail-Safe Modal Handling**: Specialized logic for handling third-party modal popups ensures uninterrupted test execution without test flakiness.

---

## 👤 Author & Acknowledgments

- **Author**: Thulasi (UDAYAKUMAR)
- **Repository**: [passport-seva-automation-testing](https://github.com/Thulasi04/passport-seva-automation-testing)
- **Framework Stack**: Python · Playwright · Pytest · Page Object Model · GitHub Actions

*Built as a production-grade automated testing showcase for resumes and portfolio review.*
