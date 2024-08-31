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
my_list_pair= [(letter,number) for letter in 'abcd' for number in range(4)]
print(my_list_pair)


"""
DICT COMPREHENSION
"""
names=['aman','dev','raj','rojit','ajay']
numb=[1,2,3,4,5]
print(list(zip(numb,names)))

"""
i want a dict{numb:'names'} for each numb,names in zip(numb,names)

my_dict_1={}
for numb,names in zip(numb,names):
	my_dict_1[numb]=names
print(my_dict_1)
"""
my_dict_2={numb:names for numb,names in zip(numb,names) if names!='dev'}
"""dont want dev printed"""
print(my_dict_2)

"""
set
"""
nums2=[1,2,3,4,5,56,4,6,2,4,1]

"""
my_set=set()
for numb in nums2:
	my_set.add(numb)
print(my_set)
"""
my_set=set()
my_set={numb for numb in nums2}
print(my_set)

"""
GENERATOR EXPRESSIONS
"""
#I want to yield 'n*n' for each 'n' in nums
nums3=[1,2,3,4,5,6,7]
def gen_func(nums3):
	for n in nums3:
		yield n*n

my_list_gen=list(gen_func(nums3))
print(my_list_gen)



