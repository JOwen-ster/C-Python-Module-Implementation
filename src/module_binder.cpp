#include <pybind11/pybind11.h>

extern "C" {
    #include "code_module.h"
}

int binder_wrapper(int x, int y) {
    return your_c_function(x, y);
}

PYBIND11_MODULE(code_module, module_) {  // Module name is "code_module"
    module_.doc() = "Module description";
    module_.def("module_function_name", &binder_wrapper, "Function description");
    // Add more functions
}