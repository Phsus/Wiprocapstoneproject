# 🛒 BrowserStack E-Commerce Automation Framework

**Wipro Python Automation Capstone Project** | **Developed by:** Sushant

This repository contains a fully automated, scalable End-to-End (E2E) testing framework built for the BrowserStack Demo E-Commerce web application. It is designed to handle modern web challenges like dynamic React components and persistent local storage.

---

## 📊 Project Presentation
A full breakdown of the architecture, challenges solved, and test strategies can be found in the project presentation.  
📄 **[View the Capstone Presentation here](./Web-Automation-using-Selenium-with-Python.pdf)** 

---

## 🚀 Key Features

* **Page Object Model (POM):** Clean separation of UI locators and test scripts for maximum maintainability.
* **Dual Data-Driven Testing (DDT):** * *External:* Uses `pandas` and `openpyxl` to inject shipping/billing data from Excel.
  * *Internal:* Uses `@pytest.mark.parametrize` for looping multiple user logins.
* **Modern Web Handling:** Utilizes CSS Selectors to bypass React auto-incrementing IDs and JavaScript to wipe `localStorage` and `sessionStorage` between test loops to prevent "ghost" sessions.
* **Parallel Execution:** Cuts execution time by running tests concurrently across multiple CPU cores using `pytest-xdist`.
* **Automated Reporting & Evidence:** Generates rich HTML reports (`pytest-html`) and automatically captures screenshots upon test failure via `conftest.py` hooks.

---

## 🛠️ Tech Stack

* **Language:** Python 3.11
* **Automation:** Selenium WebDriver
* **Test Runner:** Pytest
* **Data Management:** Pandas, OpenPyXL
* **Reporting:** Pytest-HTML

---

## ⚙️ Framework Workflow

```mermaid
graph TD
    A[Start Execution: pytest] --> B[conftest.py: Launch Chrome Browser]
    B --> C{Test Data Source}
    C -->|External DDT| D[utilities/excel_reader.py]
    C -->|Internal DDT| E[@pytest.mark.parametrize]
    D --> F[Initialize Page Objects]
    E --> F
    F --> G[Login, Home, Checkout Pages]
    G --> H[BasePage: Explicit Waits & UI Actions]
    H --> I{Assertions & Validations}
    I -->|Pass / Fail| J[conftest.py: Teardown & Screenshots]
    J --> K[Clear Session Storage & Close Browser]
    K --> L[Generate pytest-html Report]



📁 Project Structure
Plaintext
WiproCapstoneProject/
├── Pages/                  # Page Object classes (Base, Home, Login, Checkout)
├── Tests/
│   └── TestcasesPytest/    # Pytest execution scripts & conftest.py
├── utilities/              # Helper modules (Logger, Excel Reader)
├── testdata/               # External test data (testdata.xlsx)
├── reports/                # Auto-generated HTML execution reports
├── screenshots/            # Auto-captured failure evidence
├── pytest.ini              # Pytest configuration file
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
🏃 How to Run the Tests
1. Clone the repository and navigate to the directory:

Bash
git clone [https://github.com/Phsus/Wiprocapstoneproject.git](https://github.com/Phsus/Wiprocapstoneproject.git)
cd Wiprocapstoneproject
2. Install the required dependencies:

Bash
pip install -r requirements.txt
3. Generate the external test data file:

Bash
python setup_testdata.py
4. Execute the test suite:

To run normally and generate the HTML report:

Bash
pytest -s
To run in parallel (using 3 worker nodes) for faster execution:

Bash
pytest -n 3 -s
