import unittest
import HtmlTestRunner

loader = unittest.TestLoader()
suite = loader.discover('bowling', pattern='test_*.py')

runner = HtmlTestRunner.HTMLTestRunner(
    output='reports',       # folder to save reports
    report_name='unit-test-report',
    combine_reports=True,
    verbosity=2
)

runner.run(suite)
