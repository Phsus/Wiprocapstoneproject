import pytest
from selenium import webdriver
import os

driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()


    if report.when == 'call' and report.failed:
        global driver
        if driver is not None:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            file_name = f"screenshots/{item.name}_failed.png"
            driver.save_screenshot(file_name)



def pytest_metadata(metadata):
    metadata['Project'] = 'BrowserStack E-Commerce Capstone'
    metadata['Automation Engineer'] = 'Trainee'