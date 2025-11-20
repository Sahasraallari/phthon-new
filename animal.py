from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print(" I can walk and run")


class Dog(Animal):
    def move(self):
        print("I can bark")


class Snake(Animal):
    def move(self):
        print("I can Crawl")


class Lion(Animal):
    def move(self):
        print("I can Roar")


R = Human()
R.move()


P = Lion()
P.move()

R = Dog()
R.move()

K = Snake()
K.move()





