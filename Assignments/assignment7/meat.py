# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

from food import Food


class Meat(Food):

    def cook(self):
        print('The', self.name, 'has been cooked medium rare')


m = Meat('steak')

m.cook()

m2 = Meat('chicken')

m2.cook()
