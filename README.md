# playwright-python-demo

Demo project to demonstrate Playwright+Python in use

**Tools:** Playwright, Python3.8+, Pytest, Allure


# How to run

1. Create python venv:
   - `python3 -m venv myenv`
2. Activate python venv:
   - `source myenv/bin/activate`
3. Install dependencies:
   - `pip install -r requirements.txt`
4. Install playwright browsers:
   - `playwright install`
5. Run tests:
   - In terminal run this:
   - `pytest path/to/file.py`
   -
   - To run tests with allure reporting:
   - `pytest path/to/file.py --alluredir allure-results`
   - To open allure report:
   - `allure serve`
   -
   - To run tests by test name:
   - `pytest -k test_name`
   -
   - To run tests in parallel:
   - `pytest -n 5` (5 - number of threads)

**pytest.ini** - contains markers to group tests by regression, sanity or other markers
