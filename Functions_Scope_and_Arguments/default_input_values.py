'''
Python admits default input values for functions. This way, the
caller may omit those when calling the function.

A common pitfall when using default values is assigning those to
mutable input types since they are created once at function definition
time, not per call. Therefore, the mutable type variable is created
once and reused every function call.
'''

def greet(name: str="Anonymous") -> None:
    print(f"Hello {name}!")

def computePower(base: int, power: int = 2) -> int:
    return base ** power

def main():
    greet()
    print(f"computePower(10): {computePower(10)}")
    print(addItem_Wrong("A"))  # ['A']
    print(addItem_Wrong("B"))  # ['A', 'B']  ← Unexpected! Same list reused
    print(addItem("A"))
    print(addItem("B"))

def addItem_Wrong(item, container=[]):  # [] list is placed somewhere in memory, but it stays there instead of being removed afterwards.
    container.append(item)
    return container

def addItem(item, container=None):
    if container is None:
        container = []
    container.append(item)
    return container

if __name__ == "__main__":
    main()