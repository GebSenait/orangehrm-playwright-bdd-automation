# Setup Instructions

## Prerequisites
- Python 3.12.0 (or higher) installed on your system
- Access to `py` command (Windows Python launcher)

## Quick Start

### 1. Create Virtual Environment
```powershell
py -m venv venv
```

### 2. Activate Virtual Environment
**PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
.\venv\Scripts\activate.bat
```

### 3. Install Dependencies
```powershell
.\venv\Scripts\python.exe -m pip install --upgrade pip
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Install Playwright Browsers
```powershell
.\venv\Scripts\python.exe -m playwright install chromium
```

### 5. Run Tests
```powershell
.\venv\Scripts\python.exe -m behave features/
```

## Alternative: Using Python Directly

If you prefer to use Python directly without virtual environment:
```powershell
py -m pip install -r requirements.txt
py -m playwright install chromium
py -m behave features/
```

## Project Structure

- `venv/` - Virtual environment (excluded from git)
- `features/` - BDD feature files
- `steps/` - Step definitions
- `pages/` - Page Object Model classes
- `utils/` - Utility functions and configuration
- `project_config.py` - Project configuration settings

## Notes

- The virtual environment uses Python 3.12.0 from your system
- All dependencies are installed in the `venv` directory
- Screenshots are saved to `screenshots/` on test failures
- Test results are saved to `test-results/` directory

