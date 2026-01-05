"""
Step definitions for BDD scenarios

This module imports all step definitions to ensure they are discoverable.
The IDE may show warnings about undefined steps, but these are false positives.
All steps are properly defined and work correctly at runtime with Behave.

For navigation: All step definitions use exact string matching in decorators
to ensure proper linking between feature files and step definitions.
"""

# Import all step definitions to make them discoverable
# This ensures IDE can find and link steps from feature files
from steps import common_steps  # noqa: F401
from steps import search_steps  # noqa: F401
from steps import report_steps  # noqa: F401

__all__ = ['common_steps', 'search_steps', 'report_steps']
