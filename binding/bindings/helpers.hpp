#pragma once
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "highmap.hpp"

namespace py = pybind11;

// Converts a std::vector<float> to a NumPy array with a specified shape.
py::array_t<float> vector_to_numpy(const std::vector<float>  &vec,
                                   const std::vector<size_t> &size);

// Converts an hmap::Array to a NumPy array.
py::array_t<float> array_to_numpy(const hmap::Array &array);

// Converts a NumPy array to an hmap::Array.
hmap::Array numpy_to_array(const py::array_t<float> &npy);

// Converts a generic Python object to an hmap::Array.
hmap::Array pyobj_to_array(const py::object &pyobj);

// Converts a Python object (list or tuple) to hmap::Vec2<T>.
template <typename T> hmap::Vec2<T> pyobj_to_vec2(const py::object &pyobj)
{
  if ((py::isinstance<py::list>(pyobj) || py::isinstance<py::tuple>(pyobj)) &&
      py::len(pyobj) == 2)
  {
    auto pyobj_list = pyobj.cast<py::list>();
    T    x = py::cast<T>(pyobj_list[0]);
    T    y = py::cast<T>(pyobj_list[1]);
    // Return a Vec2 with the extracted values.
    return hmap::Vec2<T>(x, y);
  }
  else
    throw std::runtime_error(
        "Expected a list or tuple of two values for Vec2."); // Error if input
                                                             // is not as
                                                             // expected.
}
