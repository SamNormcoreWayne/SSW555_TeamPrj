import unittest
import os
from GED import Repository

if __name__ == "__main__":
    test_dir = os.path.join(os.getcwd(), "tests")
    print(os.getcwd())
    discover = unittest.defaultTestLoader.discover(test_dir, 'TestGED_*.py')
    docs_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    report_path = os.path.join(docs_dir, 'docs', 'report.txt')
    a = Repository(filename='Project01_Xiaomeng Xu.ged', dir_path=os.path.join(docs_dir, 'docs'))
    with open(report_path, 'w') as report:
        report.write(a.individual_pt())
        report.write(a.output_family())
        runner = unittest.TextTestRunner(stream=report, verbosity=2)
        runner.run(discover)
