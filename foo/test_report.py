import unittest
import os
from GED import Repository

if __name__ == "__main__":
    test_dir = os.path.join(os.getcwd(), "tests")
    discover = unittest.defaultTestLoader.discover(test_dir, 'TestGED_*.py')
    report_path = os.path.join(os.path.abspath(os.getcwd()), 'docs', 'report.txt')
    a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(os.path.abspath(os.getcwd()), 'docs'))
    with open(report_path, 'wb') as report:
        a.individual_pt()
        a.output_family()
        runner = unittest.TextTestRunner(stream=report, verbosity=2)
        runner.run(discover)
