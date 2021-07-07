import os
import pytest

project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
report_dir = os.path.join(project_root, 'report')
result_dir = os.path.join(report_dir, 'allure_result')
allure_report = os.path.join(report_dir, 'allure_report')
test_case_dir = os.path.join(project_root, 'test_case', 'test_dept.py')

def run_pytest():
    pytest.main(['-v', '-s', f'{test_case_dir}', f'--alluredir={result_dir}'])

def general_report():
    cmd = f'allure generate {result_dir} -o {allure_report} --clean'
    os.system(cmd)

def select_report():
    cmd = f'allure open {allure_report}'
    os.system(cmd)

if __name__ == '__main__':
    run_pytest()
    general_report()
    select_report()