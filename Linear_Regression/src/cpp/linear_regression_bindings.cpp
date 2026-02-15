/******** Include statements **********/

#include "linear_regression.hpp"
#include <pybind11/pybind11.h>  // Includes PYBIND_MODULE.
#include <pybind11/stl.h>       // Enables automatic conversion between C++ STL containers and Python objects.

/**************************************/

/******* Namespace statements *********/

namespace py = pybind11;

/**************************************/

/********** Python bindings ***********/

PYBIND11_MODULE(cpp_linear_regression, m)
    m.doc() = "C++ linear regression module (least squares)";

    m.def(  "fitLinearData"                             ,
            &fitLeastSquares2D                          ,
            "Fit linear regression using least squares" )

/**************************************/

#endif