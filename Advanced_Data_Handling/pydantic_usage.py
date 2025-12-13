from pydantic import BaseModel, Field, ValidationError
from typing import Type, TypeVar

T = TypeVar("T", bound=BaseModel)

class TrainingConfig(BaseModel):
    learning_rate: float
    epochs: int

class ConstrainedTrainingConfig(BaseModel):
    learning_rate: float = Field(..., gt=0.0)
    epochs: int = Field(..., gt=0)

def makeClassInstance(class_name: Type[T], lr: float, ep: int) -> T:
    try:
        # Use keyword args
        tct = class_name(learning_rate=lr, epochs=ep)
    except ValidationError as e:
        print(f"ValidationError caught:{e}")
        return None
    except Exception as e:
        print(f"Other exception caught: {e}")
        return None
    else:
        print(f"tct.learning_rate: {tct.learning_rate}")
        print(f"tct.epochs: {tct.epochs}")
        return tct

def main():
    makeClassInstance(TrainingConfig, "0.01", 10)
    makeClassInstance(ConstrainedTrainingConfig, "-0.01", "-3")

if __name__ == "__main__":
    main()
