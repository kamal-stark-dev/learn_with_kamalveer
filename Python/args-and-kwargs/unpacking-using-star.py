# unpacking using * 
numbers = [10, 20, 30, 40, 50]
print(numbers)
print(*numbers)

def add(*args):
    sum = 0
    for arg in args:
        sum += arg 
    return sum 

print(add(*numbers))
