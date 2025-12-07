#include <stdbool.h>
#include <stdio.h>
#include "prime_numbers.h"

bool isPrime(const int n)
{
    if(n <= 1)
        return false;
    
    for(int i = 2; i < n; i++)
        if(!(n % i))
            return false;

    return true;
}

void printPrimeNumbersInRange(const int range_start, const int range_end)
{
    for(int i = range_start; i <= range_end; i++)
        if(isPrime(i))
            printf("%d ", i);
}
