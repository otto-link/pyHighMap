#include "helpers.hpp"

py::array_t<float> vector_to_numpy(const std::vector<float>  &vec,
                                   const std::vector<size_t> &size)
{
  return py::array_t<float>(size, vec.data());
}

py::array_t<float> array_to_numpy(const hmap::Array &array)
{
  std::vector<size_t> size = {static_cast<size_t>(array.shape.x),
                              static_cast<size_t>(array.shape.y)};
  return py::array_t<float>(size, array.vector.data());
}

hmap::Array numpy_to_array(const py::array_t<float> &npy)
{
  hmap::Vec2<int> shape = {static_cast<int>(npy.shape(0)),
                           static_cast<int>(npy.shape(1))};
  hmap::Array     array = hmap::Array(shape);
  array.vector = {npy.data(), npy.data() + npy.size()};
  return array;
}

hmap::Array pyobj_to_array(const py::object &pyobj)
{
  if (py::isinstance<py::array_t<float>>(pyobj))
  {
    auto pyobj_npy = pyobj.cast<py::array_t<float>>();

    if (pyobj_npy.ndim() != 2)
      throw std::runtime_error("Expected a 2D numpy array, check shape.");

    return numpy_to_array(pyobj_npy);
  }
  else
    throw std::runtime_error("Expected a numpy array.");
}
