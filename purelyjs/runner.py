#!/usr/bin/env python

import os
import re
import sys
import time

from .io import write
from .io import writeln
from .options import parse_config
from .testmodule import TestModule


CONFIG_FILE = 'purelyjs.ini'

class TestRunner(object):
    def __init__(self, libs=None, tests=None):
        self.js_exe = 'js'
        self.regex_test_case = re.compile('^(?m)function\s+(test[A-Z][A-Z0-9a-z_]+)')

        purely_pkgroot = os.path.dirname(__file__)
        purely_js = os.path.join(purely_pkgroot, 'js', 'purely.js')

        if libs is None:
            raise ValueError("Must provide libs")
        if tests is None:
            raise ValueError("Must provide libs")

        self.libs = libs + [purely_js]
        self.tests = tests

    def find_all_test_cases(self, filepaths):
        test_cases = []

        for filepath in filepaths:
            test_cases.extend(self.find_test_cases(filepath))

        return test_cases

    def find_test_cases(self, filepath):
        with open(filepath, 'rt') as f:
            content = f.read()

        test_cases = self.regex_test_case.findall(content)
        return test_cases

    def run(self):
        test_cases = self.find_all_test_cases(self.tests)
        #self.check_test_case_uniqueness()  # TODO

        num_tests = len(test_cases)

        writeln('Running %s tests' % num_tests)
        t_start = time.time()

        modules = []
        for i, test_case in enumerate(test_cases, 1):
            module = TestModule(self.js_exe, self.libs + self.tests, test_case)
            module.run()
            modules.append((i, module))

            if module.passed:
                write('.')
            else:
                write('F')

        writeln()
        writeln()

        failed_modules = [(i, m) for (i, m) in modules if not m.passed]
        for i, module in failed_modules:
            writeln('=' * 70)
            writeln('FAILED (%s): %s' % (i, module.test_case))
            writeln('-' * 70)
            writeln(module.stderr)
            writeln()

        writeln('-' * 70)

        t_delta = time.time() - t_start
        writeln('Ran %s tests in %.3fs' % (num_tests, t_delta))

        if failed_modules:
            writeln()
            writeln('FAILED (failed=%s)' % len(failed_modules))
            return False


if __name__ == '__main__':
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('--lib', action='append')
    parser.add_option('--test', action='append')
    (options, args) = parser.parse_args()

    if os.path.exists(CONFIG_FILE):
        libs, tests = parse_config(CONFIG_FILE)

    if options.lib:
        libs = options.lib
    if options.test:
        tests = options.test

    runner = TestRunner(libs=libs, tests=tests)
    if runner.run() is False:
        sys.exit(1)
