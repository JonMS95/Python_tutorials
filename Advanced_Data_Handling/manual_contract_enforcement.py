'''
This file contains an example showing how contracts (safety, type checking)
can be manually fulfiled and why is it too "expensive".

isinstance built-in function can be used for this purpose, providing variable
(or class member) name as well as the type name or a tuple of types compatible
with the variable in question.
'''

from typing import Union

type_fi = Union[float, int]

class TrainingConfig:
    learning_rate: float
    epochs: int

    def __init__(self, learning_rate: type_fi, epochs: int) -> None:
        if not isinstance(learning_rate, (int, float)):
            raise TypeError("learning_rate must be either integer or floating-point number")
        
        if learning_rate <= 0:
            raise ValueError("learning_rate must be > 0")
        
        if not isinstance(epochs, int):
            raise TypeError("epochs must be an integer")
        
        if epochs <= 0:
            raise ValueError("epochs value must be > 0")
        
        self.learning_rate  = learning_rate
        self.epochs         = epochs

def trainModel(cfg: TrainingConfig) -> None:
    print(f"Training with learning rate: {cfg.learning_rate}, epochs: {cfg.epochs}")

def main():
    configurations: list[TrainingConfig] = [
        # TrainingConfig(learning_rate = "hello"  ,   epochs = 1      ),
        # TrainingConfig(learning_rate = -0.5     ,   epochs = 1      ),
        # TrainingConfig(learning_rate = 1.2      ,   epochs = "bye"  ),
        # TrainingConfig(learning_rate = 1.2      ,   epochs = -1     ),
        TrainingConfig(learning_rate = 1.2      ,   epochs = 1      ) # Only this configuration will work.
    ]

    for config in configurations:
        try:
            trainModel(config)
        except Exception as e:
            print(f"Caught generic exception: {e}")

if __name__ == "__main__":
    main()