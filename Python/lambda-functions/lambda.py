# Lambda Function: Sometimes you only need a tiny function once, such as when sorting or mapping data. Writing a full `def` can feel verbose (too use more words than necessary to express an idea).

# Syntax: `lambda arguments: expression` -> there is no `return` keyword because the expression is returned automatically. 

"""
def square(x):
    return x * x
print(square(10))
"""

square = lambda x: x * x
print("square(7):", square(7))

# passing multiple parameters 
add = lambda a, b: a + b 
print("add(10, 15):", add(10, 15))

# lambda with sorted()
students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 91)
]

students.sort(key=lambda student: student[1]) # tells Python to use the second elements as the sorting key.
print("Sorted Students:", students)

# lambda with map()
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# lambda with filter()
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even:", even)

# lambda with max()
top = max(students, key=lambda s: s[1])
print("Max Marks Student:", top)

"""
Avoid lambda when:
- the logic is complex
- you need multiple statements, loops or try / except 
- the function will be reused in multiple places
"""
