'''
Example file showing why dataclasses do not provide any validation mechanism.

Reminder: dataclasses are nothing but decorators provided by Python itself (built-in since 3.7 onwards).
They provide some boilerplate code for data classes (constructors, destructors, __init__, __str__ ...).
'''

from dataclasses import dataclass

@dataclass
class TrainingConfig:
    learning_rate: float
    epochs: int

def trainModel(cfg: TrainingConfig) -> None:
    print(f"Learning rate: {cfg.learning_rate}, epochs: {cfg.epochs}")

def main():
    cfg = TrainingConfig(
        learning_rate="0.01",   # Wrong type (float expected).
        epochs=-10              # Invalid value (non-negative expected).
    )                           # Nothing fails loudly, only structure is provided.
    trainModel(cfg)

if __name__ == "__main__":
    main()