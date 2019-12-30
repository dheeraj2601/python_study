export ROOT_DIR=${PWD}
LIB_DIR = lib

default: pyexamples

pyexamples: setup.py pyexamples.pyx $(LIB_DIR)/libexamples.so
	python setup.py build_ext --inplace && rm -f pyexamples.c && rm -Rf build

$(LIB_DIR)/libexamples.so:
	make -C $(LIB_DIR) libexamples.so

clean:
	rm -rf build
	rm -rf pyexamples.c
	rm -rf *.so
	rm -rf lib/*.o lib/*.a
