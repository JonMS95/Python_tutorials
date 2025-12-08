// "pip install pybind" may be required if include statement below causes trouble. 

#include <pybind11/pybind11.h>
#include "bank_account.hpp"

namespace py = pybind11;

// Change the module name to match the .so file
PYBIND11_MODULE(bank_account_bindings, m) {
    py::class_<BankAccount>(m, "BankAccount")
        .def(py::init<const std::string&, double>(),
             py::arg("owner"), py::arg("balance") = 0.0)
        .def("deposit", &BankAccount::deposit)
        .def("withdraw", &BankAccount::withdraw)
        .def("getBalance", &BankAccount::getBalance)
        .def("getOwnerName", &BankAccount::getOwnerName);
}
