import my_module as mm

courses= ['math','art','science','history','geography']

print('enter the target which you wanna find in the courses list')
target= input()
index= mm.find_index(courses,target)
if index==-1:
    print('not found in courses list')
else:
    print(f'found at index={index}')