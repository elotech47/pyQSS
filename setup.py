from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir
import pybind11

ext_modules = [
    Pybind11Extension(
        "qss_integrator.qss_py",
        [
            "qss_integrator/src/qss_python.cpp",
            "qss_integrator/src/qss_integrator.cpp",
        ],
        include_dirs=[
            "qss_integrator/src",
            pybind11.get_include(),
        ],
        cxx_std=17,
        define_macros=[('VERSION_INFO', '"dev"')],
    ),
]

setup(
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)