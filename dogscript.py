#!/usr/bin/python3

import dogsof

def main():
    d1 = dogsof.Dog("Derpy", 3, "yellow")
    d2 = dogsof.JackRussell("Eddie", 4, "mixed", False, True)

    print(d2.hunter)
    print(d2.age)

    d2.aged(3)

    print(d2.age)

    print(d1.name)

    print(d2.name)

    print(d2.rename("Larry"))

    print(d2.name)
if __name__ == "__main__":
    main()
