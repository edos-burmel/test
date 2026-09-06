def hello(*args, **kwargs):
    print("Hello, World!")
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

hello("Alice", "Bob", age=25, city="New York")