import os
import unittest
import HtmlTestRunner

# Ensure the reports folder exists
os.makedirs("reports", exist_ok=True)

# Discover all tests in the bowling folder matching test_*.py
loader = unittest.TestLoader()
suite = loader.discover('bowling', pattern='test_*.py')

# Run tests and generate HTML report
runner = HtmlTestRunner.HTMLTestRunner(
    output='reports',              # Folder to store report
    report_name='unit-test-report',  # Report file name (HTML)
    combine_reports=True,          # Combine multiple test files into one report
    verbosity=2                    # Show detailed results in console log
)

runner.run(suite)
