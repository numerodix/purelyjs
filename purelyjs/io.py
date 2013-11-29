import subprocess
import sys


def invoke(args, cwd=None):
    popen = subprocess.Popen(args, cwd=cwd,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = popen.communicate()
    out = str(out).strip()
    err = str(err).strip()
    ret = popen.returncode
    return ret == 0, err

def write(line):
    sys.stderr.write(line)
    sys.stderr.flush()

def writeln(line=''):
    if not line.endswith('\n'):
        line = '%s\n' % line
    write(line)
