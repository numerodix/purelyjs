import os
import tempfile

from .io import invoke


class TestModule(object):
    def __init__(self, js_exe, modules, test_case):
        self.js_exe = js_exe
        self.modules = modules
        self.test_case = test_case

        self.passed = None
        self.stderr = None

    def assemble(self):
        (fd, filepath) = tempfile.mkstemp(text=True)

        try:
            # concatenate modules
            for module in self.modules:
                with open(module, 'rt') as f:
                    content = f.read()

                os.write(fd, content)
                os.write(fd, '\n\n')

            # invoke the test case function
            os.write(fd, '%s();\n' % self.test_case)

        finally:
            os.close(fd)

        return filepath

    def run(self):
        filepath = self.assemble()

        try:
            passed, stderr = invoke([self.js_exe, filepath])
            if passed:
                self.passed = True

            else:
                self.passed = False
                self.stderr = stderr

        finally:
            os.unlink(filepath)
