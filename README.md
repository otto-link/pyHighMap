# HighMap python binding (pyhighmap)

This repository contains the Python bindings for the [HighMap C++
library](https://github.com/otto-link/HighMap). This package allows
you to use **a few functionalities (for now)** if HighMap directly in
your Python projects.

>[!WARNING] 
> Work in progress, use at your own risk!

## License

This project is licensed under the GNU General Public License v3.0.

## Platform Support

Currently, this package is only supported on **Linux**. Contributions
to add support for **Windows** or other platforms would be greatly
appreciated!

## Installation

To install the pyHighMap Python binding, use `pip3`:

```bash
pip3 install pyhighmap
```

## Linux Dependencies

Before installing the Python package, you may need to install some
additional dependencies on your Linux system, such as:

```bash
sudo apt install libopencv-dev libgsl-dev
```

These libraries are required for certain features within HighMap. Make
sure they are installed before proceeding with the Python package
installation.

## Example usage of HighMap in Python

### Basic noise generation

```python
import matplotlib.pyplot as plt
import pyhighmap as hmap

if __name__ == "__main__":
    shape = [256, 128]  # out numpy array shape
    frequency = [4, 2]  # spatial frequencies
    seed = 0  # random seed number

    # generate Perlin (output is a 2D numpy array)
    noise_base = hmap.noise(hmap.NoiseType.PERLIN, shape, frequency, seed)

    # fractal layering
    noise_fbm = hmap.noise_fbm(hmap.NoiseType.SIMPLEX2S, shape, frequency, seed)

    # apply filters
    noise_base = hmap.warp(noise_base, 0.1 * noise_fbm, 0.1 * noise_fbm)
    noise_fbm = hmap.falloff(noise_fbm)

    plt.figure()
    plt.imshow(noise_base, cmap='jet')

    plt.figure()
    plt.imshow(noise_fbm, cmap='terrain')

    plt.show()
```

### List available bindings

```python
import pyhighmap as hmap

if __name__ == "__main__":
    print('Available functions')
    for s in dir(hmap):
        obj = getattr(hmap, s)
        if (not s.startswith('__')) and callable(obj):
            print(' - {}'.format(s))

    print('Available base noises\n', [s for s in dir(hmap.NoiseType) \
                                      if not s.startswith('__')])
```
