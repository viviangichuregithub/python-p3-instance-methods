#!/usr/bin/env python3

class Person:
    def __init__(self, name="John Doe", age=30):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age}.")

    def change_name(self, new_name):
        self.name = new_name
        print(f"Your name has been updated to {self.name}.")

    # Required by the tests
    def talk(self):
        print("Hello World!")

    # Required by the tests
    def walk(self):
        print("The person is walking.")
        

# --- Example usage ---
if __name__ == "__main__":
    person1 = Person("Vivian", 25)
    person1.introduce()
    person1.have_birthday()
    person1.change_name("Vivi")
    person1.introduce()
    person1.talk()
    person1.walk()
