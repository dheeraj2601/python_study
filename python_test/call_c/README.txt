
https://medium.com/@shamir.stav_83310/making-your-c-library-callable-from-python-by-wrapping-it-with-cython-b09db35012a3


create examples.c

gcc -c examples.c
>> generates examples.o

ar rcs libexamples.a examples.o
>> build the static library from object files.
>> static lib named libexamples.a gets built .

In short , make Makefile




yum install python-devel
yum install numpy scipy
