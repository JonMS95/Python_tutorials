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
    cfg_input_values: list[list[type_fi, int]] = [
        ["hello"    ,   1    ],
        [-0.5       ,   1    ],
        [1.2        ,   "bye"],
        [1.2        ,   -1   ],
        [1.2        ,   1    ],
    ]

    for config in cfg_input_values:
        tcfg: TrainingConfig
        try:
            tcfg = TrainingConfig(config[0], config[1])
        except Exception as e:
            print(f"Caught generic exception: {e}")
        else:
            trainModel(tcfg)

if __name__ == "__main__":
    main()