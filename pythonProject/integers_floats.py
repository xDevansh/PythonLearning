import math
message= 1
print(type(message))
message =1.253
print(type(message))

print(dir(int))
print(dir(float))
print(round(2.6,))
print(math.floor(message))
print(math.ceil(message))

print(2+3)
print(2-3)
print(2*3)
print(2/3)
print(2//3) #// performs floor division, which means it divides the numbers and then returns the largest integer less than or equal to the quotient
print(2 % 3) #gives the remainder
print(2**3)#exponent

#comparison operators boolean variable
msg1=3
msg2=4
print(msg1==msg2)
print(msg1!=msg2)
print(msg2>msg1)
print(msg2<msg1) #   >= and <=


num1='100'
num2='200'
print(num1+num2) #cause they are strings so concatenated
#casting
num1=int(num1)
num2=int(num2)
print(num1+num2)
num3=2.6
num3=int(num3)
print(num3) #always floors

