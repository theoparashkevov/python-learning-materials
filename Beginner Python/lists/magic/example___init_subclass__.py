class MyBaseClass:
    def __init_subclass__(cls):
        print(f"A subclass of {MyBaseClass} has been created: {cls.__name__}")

class MySubClass(MyBaseClass):
    pass

# Output: "A subclass of MyBaseClass has been created: MySubClass"
