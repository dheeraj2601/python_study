cimport cython


# This file shows 4 examples:
#   - Wrapping an external c function into python, "c_hello"
#   - Making a wrapped c function on python types w/ cython syntax, "factorial"

cdef extern from "lib/cfunc.h":
    # Imports definitions from a c header file
    # Corresponding source file (cfunc.c) must be added to
    # the extension definition in setup.py for proper compiling & linking

    void hello()


def c_hello():
    # Exposes a c function to python

    hello()
