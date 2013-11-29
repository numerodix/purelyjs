from .io import invoke


class Interpreter(object):
    # Assuming whatever is called "js" on the path is likely to work best
    known_engines = ['js', 'rhino']

    def __init__(self, exes=None):
        engines = exes if exes else self.known_engines
        self.exe = self.detect(engines)

        if not self.exe:
            raise RuntimeError("No js engine could be found, tried: %s"
                               % ', '.join(engines))

    def detect(self, engines):
        found = None

        for engine in engines:
            # NOTE: Very platform specific
            success, stdout, stderr = invoke(['which', engine])

            if success:
                found = stdout
                break

        return found

    def run_module(self, filepath):
        success, stdout, stderr = invoke([self.exe, filepath])
        return success, stderr
