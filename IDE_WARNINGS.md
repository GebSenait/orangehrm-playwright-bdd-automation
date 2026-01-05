# IDE Warnings - Known Issues

## Cucumber Extension Warnings

The VS Code Cucumber extension may show warnings about "undefined steps" in `.feature` files. These are **false positives** and can be safely ignored.

### Why This Happens

- The Cucumber extension is primarily designed for JavaScript/TypeScript Cucumber implementations
- We're using **Behave** (Python BDD framework), which uses Gherkin syntax but different step definition patterns
- The extension doesn't always recognize Python step definitions correctly

### Solution

All step definitions are properly defined in:
- `steps/search_steps.py` - Search feature steps
- `steps/report_steps.py` - Reports feature steps

These steps work correctly at runtime. The warnings are cosmetic and don't affect test execution.

### To Verify Steps Are Working

Run the tests:
```powershell
.\venv\Scripts\python.exe -m behave features/
```

If tests run successfully, the step definitions are working correctly.

## Playwright Import Warnings

The type checker may show warnings about `playwright.sync_api` imports. This is because:
- Playwright is installed in the virtual environment (`venv/`)
- The IDE may not be using the correct Python interpreter

### Solution

1. **Select the correct Python interpreter:**
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose the interpreter from `venv/Scripts/python.exe`

2. **The `# type: ignore` comments** have been added to suppress these warnings

3. **The `pyrightconfig.json`** file has been configured to help the type checker find the packages

## Summary

- ✅ All step definitions are correctly implemented
- ✅ Tests run successfully
- ⚠️ IDE warnings are cosmetic and can be ignored
- ✅ Framework is fully functional

