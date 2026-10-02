# Playwright Python Pytest Passport Seva Automation Framework

This project is a Python-based UI automation framework built with Playwright and pytest for testing the Passport Seva application. It follows a Page Object Model (POM) approach to organize test logic, page actions, locators, and reusable helper functions.

The framework is designed to validate the Passport Seva application's home page, login, services, registration, appointment, and track status functionalities through automated UI test cases.

## Tech Stack

- Python
- Playwright
- pytest
- Page Object Model (POM)
- Passport Seva Application

## Project Structure

```text
passportseva/
├── helpers/
│   ├── __init__.py
│   ├── actions_for_pages.py
│   └── helper_for_pages.py
│
├── locators/
│   ├── __init__.py
│   ├── appointment_locators.py
│   ├── home_locators.py
│   ├── login_locators.py
│   ├── registration_locators.py
│   ├── services_locators.py
│   └── track_status_locators.py
│
├── pages/
│   ├── __init__.py
│   ├── appointment_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── registration_page.py
│   ├── services_page.py
│   └── track_status_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_appointment.py
│   ├── test_home.py
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_services.py
│   └── test_track_status.py
│
├── after_appointment_click.png
├── appointment_page.png
├── login_page.png
├── passport_home.png
├── passport_home_no_modal.png
├── passport_home_scrolled.png
├── registration_page.png
└── track_page.png
```
