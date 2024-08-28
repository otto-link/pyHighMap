#!/bin/bash

# directories to be formatted (recursive search)
DIRS="bindings/."
FORMAT_CMD="clang-format -style=file:scripts/clang_style -i"

# format C++
for D in ${DIRS}; do
    for F in `find ${D}/. -type f \( -iname \*.hpp -o -iname \*.cpp \)`; do
	echo ${F}
	${FORMAT_CMD} ${F}
    done
done

# python
DIRS="example"

yapf -vv --in-place --recursive setup.py

for i in ${DIRS}; do
    echo ${i}
    yapf -vv --style facebook --in-place --recursive "$i/."
done
