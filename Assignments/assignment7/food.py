# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method
# (which prints “name” and “kind” in a sentence).

# class Food:

#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind

#     def describe(self):
#         print('{} is a type of {}'.format(self.name, self.kind))


# food1 = Food('grouper', 'fish')
# food1.describe()

# food2 = Food('pork', 'meat')
# food2.describe()

# 2) Try turning describe()  from an instance method into a class and a static method.
# Change it back to an instance method thereafter.

class Food:
    name = 'shark'
    kind = 'seafood'

    @classmethod
    def describe1(cls):
        print(cls.name, 'is a type of', cls.kind)

    @staticmethod
    def describe2(name, kind):
        print(name, 'is a type of', kind)


Food.describe1()

Food.describe2('chicken', 'meat')

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

# 4) Overwrite a “dunder” method to be able to print your “Food” class.
