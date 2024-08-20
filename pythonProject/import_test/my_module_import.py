import my_module

courses= ['math','art','science','history','geography']

print('enter the target which you wanna find in the courses list')
target= input()
index= my_module.find_index(courses,target)
if index==-1:
    print('not found in courses list')
else:
    print(f'found at index={index}')