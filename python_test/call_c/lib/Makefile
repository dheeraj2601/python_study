CC = gcc 
CFLAGS = -fPIC

default: libexamples.so

libexamples.so: examples.o
	$(CC) $< -shared -o $@
#	ar rcs $@ $^
    
examples.o: examples.c examples.h 
	$(CC) -c $(CFLAGS) $<

clean:
	rm -rf *.o *.a
	rm -rf *.o *.so
