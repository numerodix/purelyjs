import optparse
import os
import sys

from .options import parse_config
from .testrunner import TestRunner


CONFIG_FILE = 'purelyjs.ini'

def main():
    parser = optparse.OptionParser()
    parser.add_option('--lib', action='append')
    parser.add_option('--test', action='append')
    parser.add_option('-v', '--verbose', action='store_true')
    (options, args) = parser.parse_args()

    libs = []
    tests = []
    verbose = options.verbose

    if os.path.exists(CONFIG_FILE):
        libs, tests = parse_config(CONFIG_FILE)

    if options.lib:
        libs = options.lib
    if options.test:
        tests = options.test

    runner = TestRunner(libs=libs, tests=tests, verbose=verbose)
    if runner.run() is False:
        sys.exit(1)


if __name__ == '__main__':
    main()
