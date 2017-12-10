#File name = zoo.py
class Animal(object):
    def __init__(self, tail, paw, wool):
        self.tail = 1
        self.paw = 4
        self.wool = True


class Dog(Animal):
    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)

    def say_woof(self):
        return 'Woof Woof'


class Cat(Animal):
    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)

    def say_meow(self):
        return 'Meow meow'


class SphynxCat(Cat):
    def __init__(self, tail, paw, wool):
        Cat.__init__(self, tail, paw, wool)
        self.wool = False

    def say_murr(self):
        return 'murr-murr'


class Rooster(Animal):
    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)
        self.paw = 2
        self.wool = False

    def say_Cocorico(self):
        return "Cocorico"

lion = Animal(tail=1, paw=4, wool=True)
dog = Dog(tail=1, paw=4, wool=True)
cat1 = Cat(tail=1, paw=4, wool=True)
cat2 = SphynxCat(tail=1, paw=4, wool=False)
rooster1 = Rooster(tail=1, paw=2, wool=False)

print (lion.paw)
print (dog.paw)
print (cat1.tail)
print (cat2.wool)
print (rooster1.paw)
print (rooster1.wool)
print (dog.say_woof())
print (cat1.say_meow())
print (cat2.say_murr())
print (rooster1.say_Cocorico())


#TEST MY CODE:

from zoo import *
import unittest

class TestZoo(unittest.TestCase):

    def test_animal(self):
        self.assertEqual(lion.tail, 1)
        self.assertEqual(lion.paw, 4)
        self.assertEqual(lion.wool, True)

    def test_dog(self):
        self.assertEqual(dog.tail, 1)
        self.assertEqual(dog.paw, 4)
        self.assertEqual(dog.wool, True)
        self.assertTrue(dog.say_woof())

    def test_cat(self):
        self.assertEqual(cat1.tail, 1)
        self.assertEqual(cat1.paw, 4)
        self.assertEqual(cat1.wool, True)
        self.assertTrue(cat1.say_meow())

    def test_sphynxcat(self):
        self.assertEqual(cat2.tail, 1)
        self.assertEqual(cat2.paw, 4)
        self.assertEqual(cat2.wool, False)
        self.assertTrue(cat2.say_murr())

    def test_rooster(self):
        self.assertEqual(rooster1.tail, 1)
        self.assertEqual(rooster1.paw, 2)
        self.assertEqual(rooster1.wool, False)
        self.assertTrue(rooster1.say_Cocorico())
if __name__ == '__main__':
    unittest.main


