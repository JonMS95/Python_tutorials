'''
Pyhton allows binding C++ libraries as well. For such purpose, pybind is strongly recommended.
'''

# cpp_binding.py
import sys
from pathlib import Path

# Ensure Python can find the shared library
lib_path = Path(__file__).parent / "cpp_lib" / "lib"
sys.path.insert(0, str(lib_path))

import bank_account_bindings as ba

# Example usage
if __name__ == "__main__":
    acc = ba.BankAccount("Alice", 1000)
    print(f"Owner: {acc.getOwnerName()}")
    print(f"Balance: {acc.getBalance()}")

    print("Depositing 500...")
    acc.deposit(500)
    print(f"Balance after deposit: {acc.getBalance()}")

    print("Withdrawing 200...")
    acc.withdraw(200)
    print(f"Balance after withdrawal: {acc.getBalance()}")

    # Uncomment to test exceptions
    # acc.withdraw(5000)
