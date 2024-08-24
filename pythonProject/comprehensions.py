lists=[1,2,3,4,5,6,7,8,9,10]
"""1) normal way
my_list=[]
# i want n for each n in lists:
for n in lists:
	my_list.append(n)
"""

my_list=[n for n in lists]
print(my_list)

"""
i want 'n' for each 'n' in lists if 'n' is even
for n in lists:
	if n%2==0:
		my_list_even.append(n):

"""
my_list_even=[n for n in lists if n%2==0]
print(my_list_even)

"""
i want 'n*n' for each 'n' in lists
for n in lists:
	if n%2==0:
		my_list_even.append(n*n):

"""
my_list_even=[n*n for n in lists]
print(my_list_even)

"""
i want a (letter,number pair) for each letter in 'abcd' and each number in 0123
my_list_pair=[]
for letter in 'abcd':
	for num in range(4):
		my_list_pair.append((letter,num))
		


"""


