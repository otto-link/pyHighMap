#!/bin/sh
HDIR='../HighMap/'
HBDIR=${HDIR}/build

INCLUDE_DIR='./include'
LIB_DIR='./lib/linux'

# headers
cp -ruv ${HDIR}/HighMap/include/* ${INCLUDE_DIR}/.

cp -uv ${HDIR}/external/delaunator/include/delaunator-cpp.hpp ${INCLUDE_DIR}/.
cp -uv ${HDIR}/external/dkm/include/dkm.hpp ${INCLUDE_DIR}/.
cp -uv ${HDIR}/external/FastNoiseLite/Cpp/FastNoiseLite.h ${INCLUDE_DIR}/.
cp -uv ${HDIR}/external/hmm/src/heightmap.h ${INCLUDE_DIR}/.
cp -uv ${HDIR}/external/hmm/src/triangulator.h ${INCLUDE_DIR}/.
cp -uv ${HDIR}/external/libnpy/include/npy.hpp ${INCLUDE_DIR}/.
cp -uv ${HDIR}/external/macro-logger/macrologger.h ${INCLUDE_DIR}/.
cp -uv ${HDIR}/external/Noise/NoiseLib/include/noise.h ${INCLUDE_DIR}/.

# libs
cp -uv ${HBDIR}/HighMap/libhighmap.a ${LIB_DIR}/.
cp -uv ${HBDIR}/external/*.a ${LIB_DIR}/.
