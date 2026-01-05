# OrangeHRM Automation Framework – Playwright + Python + BDD

**What's covered:** Search & Report validation features with 6 optimized test scenarios:
- **Search Validation (3 scenarios):** Valid employee search, invalid/no-result search, filter-based search
- **Report Generation Validation (3 scenarios):** Employee report generation, filtered report accuracy, invalid input/error handling

## How it's built (Playwright + BDD + CI)

- **Playwright with Python** – Modern, reliable browser automation
- **Behave (BDD)** – Gherkin-based behavior-driven development
- **Page Object Model** – Maintainable, reusable page abstractions
- **GitHub Actions CI** – Automated test execution on push/pull request

## Test Suite Execution Summary

**Local execution via Behave:**
```bash
pip install -r requirements.txt
playwright install chromium
behave features/
```

**CI execution on push / pull request:**
- Automated test runs via GitHub Actions
- Screenshot capture on failure
- Test results and artifacts uploaded

## What gets validated

- **Search accuracy and filters** – Employee search functionality with valid/invalid inputs and filter validation
- **Report correctness** – Report generation with data accuracy and filter consistency
- **Error handling and UI behavior** – Proper error messaging and graceful failure handling

---

**AUT:** [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com) | **Credentials:** Admin / admin123

