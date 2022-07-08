# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method
# (which prints “name” and “kind” in a sentence).
# 4) Overwrite a “dunder” method to be able to print your “Food” class.

class Food:

    def __init__(self, name, kind=0):
        self.name = name
        self.kind = kind

    def __repr__(self):
        return str('This is ' + self.name + ' and it is a type of ' + self.kind)

    def describe(self):
        print('{} is a type of {}'.format(self.name, self.kind))


food1 = Food('grouper', 'fish')
food1.describe()
print(food1)

food2 = Food('noodle', 'carbohydrate')
food2.describe()
print(food2)


# 2) Try turning describe()  from an instance method into a class and a static method.
# Change it back to an instance method thereafter.

class Food:
    name = 'stingray'
    kind = 'seafood'

    @classmethod
    def describe1(cls):
        print(cls.name, 'is a type of', cls.kind)

    @staticmethod
    def describe2(name, kind):
        print(name, 'is a type of', kind)


Food.describe1()

Food.describe2('rice', 'carbohydrate')
