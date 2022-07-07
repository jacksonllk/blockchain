
# basic method of setting and getting attributes in python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# instantiate a new object
human = Celsius()

# set the temperature
human.temperature = 37

# print the temperature
print(human.temperature)

# go to the fahrenheit method
print(human.to_fahrenheit())
