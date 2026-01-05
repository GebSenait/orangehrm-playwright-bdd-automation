# Step Definition Navigation Guide

## ✅ Step Definitions Are Now Fully Linked and Navigable

All steps in `features/search.feature` and `features/reports.feature` are now properly linked to their step definitions in the `steps/` directory, which in turn call methods in the `pages/` directory.

## How to Navigate Steps in VS Code

### Method 1: Hover and Click (Recommended)
1. Open any `.feature` file (e.g., `features/search.feature`)
2. **Hover** over any step (Given/When/Then/And)
3. You'll see a tooltip showing the step definition location
4. **Ctrl+Click** (Windows/Linux) or **Cmd+Click** (Mac) to navigate directly

### Method 2: Go to Definition
1. Place your cursor on any step in a feature file
2. Press **F12** or right-click → "Go to Definition"
3. Navigate directly to the step definition function

### Method 3: Find All References
1. Right-click on a step definition function in `steps/*_steps.py`
2. Select "Find All References" (Shift+F12)
3. See all places where the step is used in feature files

## Navigation Flow

```
Feature File (features/*.feature)
    ↓ Ctrl+Click on step
Step Definition (steps/*_steps.py)
    ↓ Function calls
Page Object Method (pages/*_page.py)
```

## Example Navigation Path

**Feature File:**
```gherkin
When I search for an employee with name "John"
```

**Step Definition (steps/search_steps.py):**
```python
@when('I search for an employee with name "{employee_name}"')
def step_search_employee(context, employee_name):
    """
    Linked to: pages/search_page.py -> SearchPage.search_by_employee_name()
    """
    context.search_page.search_by_employee_name(employee_name)
```

**Page Object (pages/search_page.py):**
```python
def search_by_employee_name(self, employee_name: str):
    """Search for employee by name"""
    # Implementation...
```

## Step Mapping Summary

### Search Feature Steps
- All steps in `features/search.feature` → `steps/search_steps.py` → `pages/search_page.py`
- Login step → `steps/common_steps.py` → `pages/login_page.py`

### Reports Feature Steps
- All steps in `features/reports.feature` → `steps/report_steps.py` → `pages/reports_page.py`
- Login step → `steps/common_steps.py` → `pages/login_page.py`

## VS Code Extensions Required

For best navigation experience, install one of these extensions:

1. **Cucumber (Gherkin) Full Support** (recommended)
   - Extension ID: `alexkrechik.cucumberautocomplete`
   - Provides step navigation and autocomplete

2. **Gherkin** (alternative)
   - Extension ID: `stevejpurves.cucumber`
   - Basic Gherkin syntax support

## Troubleshooting

### If Navigation Doesn't Work:

1. **Reload VS Code Window:**
   - Press `Ctrl+Shift+P`
   - Type "Developer: Reload Window"
   - Press Enter

2. **Check Python Interpreter:**
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose: `.\venv\Scripts\python.exe`

3. **Verify Extension is Installed:**
   - Press `Ctrl+Shift+X` to open Extensions
   - Search for "Cucumber" or "Gherkin"
   - Install if not already installed

4. **Check Step Text Matches:**
   - Step text in feature file must match decorator text exactly
   - Case-sensitive matching
   - Parameter placeholders must match: `"{name}"` in both places

## Quick Reference

| Action | Shortcut |
|--------|----------|
| Go to Definition | F12 |
| Find All References | Shift+F12 |
| Navigate with Click | Ctrl+Click / Cmd+Click |
| Reload Window | Ctrl+Shift+P → "Reload Window" |

## Documentation Files

- **STEP_DEFINITIONS_MAP.md** - Complete mapping of all steps to definitions
- **NAVIGATION_GUIDE.md** - This file (navigation instructions)
- **.vscode/settings.json** - VS Code configuration for step navigation

## Verification

To verify navigation is working:

1. Open `features/search.feature`
2. Hover over `Given I am logged into OrangeHRM`
3. You should see a tooltip
4. Ctrl+Click should take you to `steps/common_steps.py` line 10
5. From there, you can see it calls `pages/login_page.py`

All steps are now properly linked and navigable! 🎉

