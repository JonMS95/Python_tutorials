#include "bank_account.hpp"

BankAccount::BankAccount(const str& owner_name, const double initial_balance):
    name(owner_name), balance(initial_balance)
{
    if(owner_name.empty())
        throw inv_arg("Owner name cannot be empty.");
    
    if(initial_balance < 0)
        throw inv_arg("Initial balance cannot be negative.");
}

void BankAccount::deposit(const double amount)
{
    if(amount <= 0)
        throw inv_arg("Deposit cannot be negative nor zero.");
    
    this->balance += amount;
}

void BankAccount::withdraw(const double amount)
{
    if(amount <= 0)
        throw inv_arg("Withdrawal cannot be negative nor zero.");
    
    if(amount > balance)
        throw run_err("Insufficient funds.");
    
    balance -= amount;
}

double BankAccount::getBalance(void) const noexcept
{
    return this->balance;
}

std::string BankAccount::getOwnerName(void) const noexcept
{
    return this->name;
}

BankAccount::~BankAccount(void)
{
    if(this->balance)
        std::cout << "Cannot delete bank account with balance greater than zero." << std::endl;
    
    std::cout << "Destroying bank account (owner: " << this->name << ")." << std::endl;
}