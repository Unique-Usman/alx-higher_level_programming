class MyClass:
    class_attribute = 10

    def __init__(self):
        self.instance_attribute = 20

obj = MyClass()
print(obj.__class__.__dict__)
