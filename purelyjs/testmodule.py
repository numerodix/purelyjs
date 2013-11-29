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
        self.filepath = None

    def assemble(self):
        (fd, self.filepath) = tempfile.mkstemp(text=True)

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

    def run(self):
        self.assemble()

        try:
            passed, stderr = invoke([self.js_exe, self.filepath])
            if passed:
                self.passed = True

            else:
                self.passed = False
                self.stderr = stderr

        finally:
            os.unlink(self.filepath)
