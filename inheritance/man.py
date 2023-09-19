class MyClass:
    __protected_attribute = 42

obj = MyClass()
print(obj._MyClass__protected_attribute)  # This will raise an AttributeError

