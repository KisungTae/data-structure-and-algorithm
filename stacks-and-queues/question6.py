# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linkedlist data structure.

from datetime import date, datetime
from datetime import timedelta

class Stack:

    def __init__(self):
        self.stack = []
    
    def add(self, data):
        self.stack.insert(0, data)

    def pop(self):
        return self.stack.pop(0)
    
    def is_empty(self):
        return len(self.stack) <= 0

    def peek(self):
        return self.stack[0]


class Cat:

    def __init__(self, name, date):
        self.name = name
        self.date = date

class Dog:
    
    def __init__(self, name, date):
        self.name = name
        self.date = date


class Shelter:

    def __init__(self):
        self.__cats = Stack()
        self.__dogs = Stack()
    
    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.__enqueue(animal, self.__cats)
        elif isinstance(animal, Dog):
            self.__enqueue(animal, self.__dogs)
    
    def __enqueue(self, animal, stack):
        buffer = Stack()
        while not stack.is_empty() and animal.date > stack.peek().date:
            buffer.add(stack.pop())
        
        stack.add(animal)
        
        while not buffer.is_empty():
            stack.add(buffer.pop())
    
    def dequeue_any(self):
        cat = self.__cats.peek()
        dog = self.__dogs.peek()
        if cat.date > dog.date:
            return cat
        else:
            return dog
    
    def dequeue_dog(self):
        print("dequeue_dog")

    def dequeue_cat(self):
        print("dequeue_cat")

    def print_dogs(self):
        for dog in self.__dogs.stack:
            print(dog.name + " : " + str(dog.date))
    
    def print_cats(self):
        for cat in self.__cats.stack:
            print(cat.name + " : " + str(cat.date))
            



shelter = Shelter()

now = datetime.now()

for i in range (10):
    dog = Dog("dog-" + str(i), now)
    shelter.enqueue(dog)
    now = now - timedelta(minutes = 10)

now = datetime.now()

for i in range (10):
    cat = Cat("cat-" + str(i), now)
    shelter.enqueue(cat)
    now = now - timedelta(minutes = 10)



shelter.print_dogs()
shelter.print_cats()
print(shelter.dequeue_any().name)