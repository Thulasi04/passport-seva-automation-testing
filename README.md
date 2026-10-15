#  Passport Seva UI Automation Testing Framework

##  Project Overview

The Passport Seva UI Automation Testing Framework is a Python-based automation project designed to validate key functionalities of the official [Passport Seva Portal](https://www.passportindia.gov.in/psp).

The framework uses **Playwright, Pytest, and the Page Object Model (POM)** to organize test cases, improve code reusability, and automate browser-based functional testing. It also supports automated HTML reporting, failure screenshot capture, and continuous integration using GitHub Actions.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Automation Tool:** Playwright
- **Test Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** Pytest HTML
- **CI/CD:** GitHub Actions
- **Version Control:** Git and GitHub

## 🎯 Testing Scope

The framework covers the following functional modules:

- **Home Page:** Page loading, navigation links, search bar, and accessibility controls.
- **Login:** Pre-login navigation and login field interactions.
- **Registration:** Registration form validation, field interactions, and reset functionality.
- **Appointment Availability:** Passport office selection, form interactions, and reset functionality.
- **Passport Services:** Verification of passport schemes and service information.
- **Application Tracking:** Application type selection, file number entry, date of birth interaction, and form reset.

## 🏗️ Framework Features

- **Page Object Model (POM):** Separates page actions, locators, and test logic for easier maintenance.
- **Reusable Helpers:** Provides reusable methods for clicking, typing, selecting elements, navigation, and assertions.
- **Pytest Fixtures:** Supports consistent browser setup and test execution.
- **Automated HTML Reports:** Generates test execution reports with results and failure details.
- **Failure Screenshots:** Captures screenshots when automated tests fail.
- **Test Organization:** Groups test cases by functional modules and Pytest markers.
- **Parallel Execution:** Supports running tests in parallel using `pytest-xdist`.
- **CI/CD Integration:** Uses GitHub Actions to execute tests automatically on pushes and pull requests.

## 📂 Project Structure

```text
passport-seva-automation-testing/
├── .github/
│   └── workflows/
│       └── playwright.yml
├── helpers/
│   ├── actions_for_pages.py
│   └── helper_for_pages.py
├── locators/
│   ├── appointment_locators.py
│   ├── home_locators.py
│   ├── login_locators.py
│   ├── registration_locators.py
│   ├── services_locators.py
│   └── track_status_locators.py
├── pages/
│   ├── appointment_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── registration_page.py
│   ├── services_page.py
│   └── track_status_page.py
├── reports/
│   ├── report.html
│   ├── passed/
│   └── failed/
├── tests/
│   ├── conftest.py
│   ├── test_appointment.py
│   ├── test_home.py
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_services.py
│   └── test_track_status.py
├── pytest.ini
├── requirements.txt
└── README.md
```

