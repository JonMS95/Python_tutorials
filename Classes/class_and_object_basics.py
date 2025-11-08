'''
Same as in other languages, classes in Python do include methods and members.
Those methods can be custom or built-in, since every class in Python inherits
from a common superclass namely "object". "__init__" method, for instance, is
defined originally within "object" class.

To refer to the class within itself, use "self" keyword.

Classes can be defined explicitly in Python in separated sections. however,
they can also be defined as class members. Use "self" keyword to retrieve them,
same as for class methods.

Also, note that every method within class' definition takes self as input
parameter (representing the instance itself). Beneath classes there are just
namespaces in Python.

After having read about classes and constructors, the question arises naturally:
may destructors be defined in Python? Well, they can, but since Python has a
built-in garbage collector, its usage is simply not encouraged. Defining it will
definitely not break anything, but timing is uncertain. TL;DR: define it only for
additional cleanup, avoid explicit calls.
'''

class Sensor:
    def __init__(self, name: str, value: float = 0.0):  # Constructor method
        self.name = name    # Class members
        self.value = value
    
    # User-defined methods below.
    def read(self) -> float:
        return self.value

    def getSensorName(self) -> str:
        return self.name

    def updateSensorReading(self, new_value: float) -> None:
        self.value = new_value
    
    def __del__(self):
        print(f"Destroying sensor with name: {self.name}")

# Create class objects using the syntax below.

def main():
    t_sensor = Sensor("temp_sensor")
    t_sensor.updateSensorReading(12.34)
    print(f"Sensor name: {t_sensor.getSensorName()}, read temperature: {t_sensor.read()}")

if __name__ == "__main__":
    main()