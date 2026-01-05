"""
Step definitions for BDD scenarios

This module imports all step definitions to ensure they are discoverable.
The IDE may show warnings about undefined steps, but these are false positives.
All steps are properly defined and work correctly at runtime with Behave.
"""

# Import all step definitions to make them discoverable
from steps import search_steps  # noqa: F401
from steps import report_steps  # noqa: F401

__all__ = ['search_steps', 'report_steps']
