'''
This dummy example just shows why dicts are not safe by nature.
'''

from typing import Union

type_fi = Union[float, int]

def train_model(config: dict[str, type_fi]) -> None:
    # Assumes config has correct shape (i.e., expected members).
    lr = config["learning_rate"]
    ep = config["epochs"]

    print(f"Training with learning rate: {lr}, epochs: {ep}")

def main():
    configurations: list[dict[str, type_fi]] = [
        # Missing key -> late crash (during runtime).
        {
            "learning_rate" :   0.01
        },
        # Wrong type -> silent logic error.
        {
            "learning_rate" :   "0.01"  ,
            "epochs"        :   10
        },
        # Semantically invalid -> passes silently (makes sense within program's scope but not IRL).
        {
            "learning_rate" :   -0.5    ,
            "epochs": 10
        }
    ]

    for c in configurations:
        try:
            train_model(c)
        except Exception as e:
            print(f"Generic exception caught: {e}")

if __name__ == "__main__":
    main()