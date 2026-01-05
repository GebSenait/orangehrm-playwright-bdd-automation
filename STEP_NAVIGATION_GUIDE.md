# Step Definition Navigation Guide

## Overview

This guide explains how to enable navigation from Cucumber feature files to their corresponding step definitions in Python Behave.

## IDE Configuration

### VS Code Setup

1. **Install Required Extensions:**
   - Cucumber (Gherkin) Full Support Extension
   - Python Extension

2. **Configuration Files:**
   - `.vscode/settings.json` - Configured for step definition discovery
   - `behave.ini` - Behave configuration with step definitions path
   - `steps/__init__.py` - Imports all step definitions for discoverability

### How Navigation Works

1. **Hover over steps** in `.feature` files to see step definition locations
2. **Ctrl+Click** (or Cmd+Click on Mac) on any step to navigate to its definition
3. **Go to Definition** (F12) works on steps in feature files

### Step Definition Structure

All step definitions are organized as follows:

```
steps/
├── __init__.py          # Imports all step definitions
├── common_steps.py      # Shared steps (e.g., login)
├── search_steps.py      # Search feature steps
└── report_steps.py      # Report feature steps
```

### Step Matching

Behave uses exact string matching for step definitions. The decorator text must match the step text in the feature file exactly (case-sensitive).

Example:
- Feature file: `Given I am logged into OrangeHRM`
- Step definition: `@given('I am logged into OrangeHRM')`

### Troubleshooting

If navigation doesn't work:

1. **Reload VS Code Window:**
   - Press `Ctrl+Shift+P`
   - Type "Developer: Reload Window"

2. **Check Python Interpreter:**
   - Press `Ctrl+Shift+P`
   - Type "Python: Select Interpreter"
   - Choose: `.\venv\Scripts\python.exe`

3. **Verify Step Definitions:**
   - Ensure step text in feature file matches decorator text exactly
   - Check that step definition files are in the `steps/` directory
   - Verify `steps/__init__.py` imports all step definition modules

4. **Extension Settings:**
   - Open VS Code Settings
   - Search for "cucumber"
   - Verify "Cucumber: Glue" points to `steps/**/*.py`

### Manual Navigation

If IDE navigation doesn't work, you can manually find step definitions:

1. Search for the step text in the codebase
2. Use `grep` or VS Code search: `Ctrl+Shift+F`
3. Search for the step text (e.g., "I am logged into OrangeHRM")

### Step Definition Locations

| Step Text | File | Function |
|-----------|------|----------|
| `I am logged into OrangeHRM` | `steps/common_steps.py` | `step_login_common` |
| `I navigate to the Employee List page` | `steps/search_steps.py` | `step_navigate_to_employee_list` |
| `I navigate to the Reports page` | `steps/report_steps.py` | `step_navigate_to_reports` |
| `I search for an employee with name "<name>"` | `steps/search_steps.py` | `step_search_employee` |
| `I generate an employee report` | `steps/report_steps.py` | `step_generate_report` |

## Scenario Outlines

The feature files now use **Scenario Outlines** for data-driven testing:

- `features/search.feature` - Contains 3 Scenario Outlines with Examples tables
- `features/reports.feature` - Contains 1 Scenario Outline with Examples table

This allows testing multiple data combinations efficiently.

