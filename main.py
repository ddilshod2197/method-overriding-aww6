class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

def main():
    dog = Dog("Buldoq")
    cat = Cat("Mursik")

    print(dog.sound())  # Woof!
    print(cat.sound())  # Meow!

if __name__ == "__main__":
    main()
```

```python
class BaseClass:
    def method(self):
        print("Base class method")

class DerivedClass(BaseClass):
    def method(self):
        print("Derived class method")

def main():
    base = BaseClass()
    derived = DerivedClass()

    base.method()  # Base class method
    derived.method()  # Derived class method

if __name__ == "__main__":
    main()
