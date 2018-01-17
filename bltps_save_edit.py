#! /usr/bin/env python2

import sys
import traceback
from borderlands.bltps import AppTPS

if __name__ == "__main__":
    try:
        app = AppTPS(sys.argv[1:])
        app.run()
    except Exception, e:
        print >>sys.stderr, "Something went wrong, but please ensure you have the latest "
        print >>sys.stderr, "version from https://github.com/apocalyptech/borderlands2 before "
        print >>sys.stderr, "reporting a bug.  Information useful for a report follows:"
        print >>sys.stderr
        print >>sys.stderr, repr(sys.argv)
        print >>sys.stderr
        traceback.print_exc(None, sys.stderr)
