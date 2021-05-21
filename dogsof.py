#!/usr/bin/python3

class Dog:
    def __init__(self, name, age, color):
        self.name = name.capitalize()
        self.age = age
        self.color = color.lower()

    def __str__(self):
        return f"{self.name}"

    def aged(self, yearsolder):
        """age our dog object"""
        self.age = self.age + yearsolder  # take the current age "n", and add in the age passed to .aged(n)
        return None

    def rename(self, newname):
        """assign a new name to the dog"""
        self.name = newname.capitalize()
        return self.name

class JackRussell(Dog):
    def __init__(self, name, age, color, isWirehair, isHunter):
        Dog.__init__(self, name, age, color)
        self.wirehair = isWirehair
        self.hunter = isHunter

def main():
    d1 = Dog("fido", 2, "brown")
    print(d1)

if __name__ == "__main__":
    main()
