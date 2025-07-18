from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext
import pybind11


ext_modules = [
    Pybind11Extension(
        'module_name',
        [
            'src/module_binder.cpp',
            'src/code_module.c',
        ],
        include_dirs=[
            pybind11.get_include(),
            'include/',
        ],
        language="c++",
        cxx_std=11, # version
    ),
]

setup(
    name='modeule_name',
    version="1.0.0",
    author="author",
    author_email="email@example.com",
    description="Module description",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        "pybind11>=3.0.0",
    ],
)