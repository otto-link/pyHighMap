cmake_minimum_required(VERSION 3.13)
project(pyhighmap LANGUAGES CXX)

# find pybind11
find_package(pybind11 REQUIRED)

# set the C++ standard
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# create the Python module
set(SOURCES
    bindings/bindings.cpp
    bindings/helpers.cpp
)

pybind11_add_module(pyhighmap ${SOURCES})

target_include_directories(pyhighmap PRIVATE ${PROJECT_SOURCE_DIR}/include)

# dependencies
find_package(OpenCV REQUIRED)
target_link_libraries(pyhighmap PRIVATE ${OpenCV_LIBS})

target_link_libraries(pyhighmap PRIVATE ${PROJECT_SOURCE_DIR}/lib/linux/libhighmap.a)

# Add a custom target to run setup.py
set(BUILD_MODULE_DIR "${CMAKE_BINARY_DIR}/build_module")

add_custom_target(create_module_builtdir ALL
    COMMAND ${CMAKE_COMMAND} -E make_directory ${BUILD_MODULE_DIR}
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${PROJECT_SOURCE_DIR}/bindings ${BUILD_MODULE_DIR}/bindings
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${PROJECT_SOURCE_DIR}/include  ${BUILD_MODULE_DIR}/include
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${PROJECT_SOURCE_DIR}/lib  ${BUILD_MODULE_DIR}/lib
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${PROJECT_SOURCE_DIR}/pyhighmap  ${BUILD_MODULE_DIR}/pyhighmap
    COMMAND ${CMAKE_COMMAND} -E copy ${PROJECT_SOURCE_DIR}/setup.py ${BUILD_MODULE_DIR}
    COMMAND ${CMAKE_COMMAND} -E copy ${PROJECT_SOURCE_DIR}/example/main.py ${BUILD_MODULE_DIR}
    # COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:pyhighmap> ${BUILD_MODULE_DIR}/pyhighmap/
)

add_custom_target(build_python_module ALL
    COMMAND ${CMAKE_COMMAND} -E make_directory ${BUILD_MODULE_DIR}
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:pyhighmap> ${BUILD_MODULE_DIR}/pyhighmap/

    WORKING_DIRECTORY ${BUILD_MODULE_DIR}
    COMMAND ${PYTHON_EXECUTABLE} setup.py build
    COMMAND ${PYTHON_EXECUTABLE} setup.py sdist bdist_wheel
    
    DEPENDS pyhighmap
    DEPENDS create_module_builtdir
)

add_custom_target(build_wheel_with_docker ALL
    COMMAND ${CMAKE_COMMAND} -E copy ${PROJECT_SOURCE_DIR}/scripts/wheel/build_module_wheel.sh ${BUILD_MODULE_DIR}
    COMMAND ${CMAKE_COMMAND} -E copy ${PROJECT_SOURCE_DIR}/scripts/wheel/Dockerfile ${BUILD_MODULE_DIR}
    
    WORKING_DIRECTORY ${BUILD_MODULE_DIR}
    COMMAND ./build_module_wheel.sh
    DEPENDS create_module_builtdir
)

add_custom_target(export_wheel ALL
    WORKING_DIRECTORY ${BUILD_MODULE_DIR}
    COMMAND twine upload dist/*
    DEPENDS build_wheel_with_docker
)
