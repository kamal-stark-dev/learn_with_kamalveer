# *args -> to pass an arbitrary number of positional arguments
def foo(*args):
    print("args:", args)
    print(type(args))
    
    return sum(args)

print("sum(1, 2, 3, 4):", foo(1, 2, 3, 4))
print("sum(10, 20):", foo(10, 20))
print()

# **kwargs -> to pass an arbitrary number of keyword arguments (collects keyword arguments into a dictionary)
def foo_2(**kwargs):
    print("keyword args:", kwargs)
    print(type(kwargs))

    for keyword, value in kwargs.items():
        print(keyword, value)

foo_2(x=10, y=20)
foo_2(name="Jake", age=20, isAdult=True)
print()

# using both *args and **kwargs 
def foo_3(*positional_args, **keyword_args):
    print("Positional Arguments: ", positional_args)
    print("Keyword Arguments: ", keyword_args)

foo_3("Hello", 100, [1, 2, 3], name="Jake", age=21)
print()

# mixing normal arguments and *args 
def foo_4(anime, *characters):
    print("Anime:", anime)
    print("Characters:")
    i = 1 
    for character in characters:
        print(f"{i}. {character}")
        i += 1

foo_4("One-Piece", "Luffy", "Zoro", "Nami", "Ussop", "Sanji", "Chopper", "Robin", "Franky", "Brook", "Jimbei")
print()

# using both together
def foo_5(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

foo_5("Jake", [1, 2, 3], False, (10, 20), 3.14, name="Jake", age=21)
