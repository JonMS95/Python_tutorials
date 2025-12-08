#include <iostream>
#include <string>
#include <stdexcept>

class BankAccount
{
private:
    using str       = std::string;
    using inv_arg   = std::invalid_argument;
    using run_err   = std::runtime_error;

    const str name;
    double balance = 0;

public:
    BankAccount(void) = delete;
    BankAccount(const str& owner_name, const double initial_balance = 0.0);
    void deposit(const double amount);
    void withdraw(const double amount);
    double getBalance(void) const noexcept;
    str getOwnerName(void) const noexcept;
    virtual ~BankAccount(void);
};