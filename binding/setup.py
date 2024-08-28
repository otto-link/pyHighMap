from setuptools import setup, Extension
import pybind11
import os
import platform
import shutil

# Determine the current platform
system = platform.system().lower()

# Set platform-specific library and include directories
if system == 'linux':
    library_dirs = ['lib/linux']
    libraries = ['opencv_core', 'opencv_imgcodecs']
    extra_objects = ['lib/linux/libhighmap.a']
    other_include_dirs = ['/usr/include/opencv4/', 'bindings']
elif system == 'windows':
    #TODO
    pass

ext_modules = [
    Extension('pyhighmap', ['bindings/bindings.cpp', 'bindings/helpers.cpp'],
              include_dirs=[pybind11.get_include(), 'include'] +
              other_include_dirs,
              library_dirs=library_dirs,
              libraries=libraries,
              extra_objects=extra_objects,
              language='c++'),
]

setup(
    name='pyhighmap',
    version='0.0.0',
    description='Python bindings for HighMap',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    author='Otto Link',
    author_email='otto.link.bv@gmail.com',
    url='https://github.com/otto-link/pyHighMap',
    license='GPLv3',
    ext_modules=ext_modules,
    packages=['pyhighmap'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C++',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Linux',
    ],
    python_requires='>=3.6',
)

# --- move .so file
source_dir = '.'
dest_dir = 'pyhighmap'

# Ensure the destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# Move all .so files from source_dir to dest_dir
for filename in os.listdir(source_dir):
    if filename.endswith('.so'):
        shutil.move(os.path.join(source_dir, filename),
                    os.path.join(dest_dir, filename))
