from __future__ import print_function

def err_exit(*arg, **kwargs):
    print(*arg, file=sys.stderr, **kwargs)
    sys.exit(1)

def print_err(*arg, **kwargs):
    print(*arg, file=sys.stderr, **kwargs)
