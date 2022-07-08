# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

from food import Food


class Fruit(Food):

    def clean(self):
        print('The', self.name, 'has been cleaned with water')


f = Fruit('apple')

f.clean()
