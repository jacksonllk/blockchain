# making getter and setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        # if value < -273.15:
        #     raise ValueError("temperature below -273.15 is not possible")
        self._temperature = value


# instantiate a new object, set_temperature internally called by __init__
human = Celsius(37)

# get the temperature attribute via a getter
print(human.get_temperature())

# get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
human.set_temperature(-300)

# get the to_fahrenheit method
print(human.to_fahrenheit())
