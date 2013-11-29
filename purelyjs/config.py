import ConfigParser
import re


def parse_config(filepath):
    cfg = ConfigParser.ConfigParser()
    cfg.read(filepath)

    section_name = 'purelyjs'

    if not cfg.has_section(section_name):
        raise ValueError("No section %s found" % section_name)

    libs = []
    tests = []

    for key, value in cfg.items(section_name):
        if key == 'libs':
            libs = re.split('\s+', value)
        elif key == 'tests':
            tests = re.split('\s+', value)

    libs = [lib for lib in libs if lib]
    tests = [test for test in tests if test]

    return libs, tests
