#!/usr/bin/env python3

class Dog:
    # Constructor method with default values for testing compatibility
    def __init__(self, name="Fido", breed="Mutt"):
        self.name = name
        self.breed = breed

    # Instance method: bark (must match test output exactly)
    def bark(self):
        print("Woof!")

    # Instance method: sit (must match test output exactly)
    def sit(self):
        print("The dog is sitting.")

    # Instance method: roll over (no test given, so we can keep it flexible)
    def roll_over(self):
        print(f"{self.name} is rolling over!")


# Manual testing (will not affect pytest)
if __name__ == "__main__":
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Max", "German Shepherd")

    dog1.bark()
    dog1.sit()
    dog2.roll_over()
