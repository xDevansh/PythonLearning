def hello_func():
    pass #dont wanna do anything for now in this func

print(hello_func)
print(hello_func())
print('======')

def hello(state='undefined'): #passed a default value if state not mentioned
    print(f'hello state={state}')

for state in range(4):
    hello(state)
print('======')
def hello1():
    return 'bye'
print(hello1().upper())
print('======')

# Positional Arguments:
# Positional arguments are the most common type of arguments in Python.
#When you call a function, you pass arguments in the same order as the function's parameters.
#The order of the arguments matters.
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

greet("Alice", 30)  # Positional arguments: "Alice" -> name, 30 -> age
print('======')
#Keyword Arguments
#Keyword arguments are passed to a function by explicitly specifying the parameter name.
#The order of arguments does not matter since each argument is paired with a parameter name.
#They make the function call more readable, especially when the function has many parameters or when default values are used.
def greet(name, age):
    print(f"Hello, my name is {name} and I am {age} years old.")

greet(age=30, name="Alice")  # Keyword arguments: age=30, name="Alice"

#positional args should come before keyword args
print('======')

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info('MATHS','ART',NAME='DEVANSH',AGE=19) #returns a tuple and a dict
print('======')

courses=['Math','Art']
info={'name':'devansh','age':19}
def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info(*courses,**info)





