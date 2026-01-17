'''
(Disclaimer: this lesson may feel a bit more theoretical than usual)

The core idea that should be kept here is that floating-point arithmetic is just an
approximation. Therefore, fast code that ignores this may end up being silently wrong.

Numerical stability is commonly attributed to algorithms that keep those rounding
errors bounded and do not grow endlessly and remain accurate to an extent.
NumPy is fast, but it does not protect anyone from these errors (and it should not be
held accountable for it).

However, NumPy provides mechanisms for us to compare numbers that are "mathematically
equal", it's to say, for those which are expected to meet a result mathematically
although it should not be that way in program's memory (due to how IEEE-754 works).
Use .isclose for scalars and .allclose for ndarrays. Try not use "==" if 
'''

import numpy as np

def roundingErrorExample() -> None:
    a: float = 0.1
    b: float = 0.2
    c: float = a + b
    expected: float = 0.3

    print(f"c (= a + b): {c}, expected: {expected}")
    print(f"c == expected -> {(c == expected)}")
    print(f"np.isclose(c, expected) -> {np.isclose(c, expected)}")

def overflowExample() -> None:
    x: np.ndarray = np.array([1000.0])
    print(np.exp(x))

def underflowExample() -> None:
    x: np.ndarray = np.array([-1000.0])
    print(np.exp(x))

def catastrophicCancellationExample() -> None:
    x: int = 1e+16 + 1
    y: int = 1e+16
    z = x - y
    print(f"x: (1e+16 + 1), y: (1e+16), z (a - b): {z}")

def main():
    roundingErrorExample()
    overflowExample()
    underflowExample()
    catastrophicCancellationExample()

if __name__ == "__main__":
    main()