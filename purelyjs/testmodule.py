import os
import tempfile

from .io import invoke


class TestModule(object):
    def __init__(self, testdir, js_exe, modules, test_case, keep_module=False):
        self.testdir = testdir
        self.js_exe = js_exe
        self.modules = modules
        self.test_case = test_case
        self.keep_module = keep_module

        self.passed = None
        self.stderr = None
        self.filepath = None

    def assemble(self):
        (fd, self.filepath) = tempfile.mkstemp(
            dir=self.testdir,
            prefix='%s_' % self.test_case,
            suffix='.js',
            text=True,
        )

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
            if not self.keep_module:
                os.unlink(self.filepath)
