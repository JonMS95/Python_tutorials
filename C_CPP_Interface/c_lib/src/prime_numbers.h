#ifndef PRIME_NUMBERS
#define PRIME_NUMBERS

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>

#define PRIME_NUMBERS_API   __attribute__((visibility("default")))

PRIME_NUMBERS_API bool isPrime(const int n);
PRIME_NUMBERS_API void printPrimeNumbersInRange(const int range_start, const int range_end);

#ifdef __cplusplus
}
#endif

#endif