#lists

course=[]
course.append('hello')
print(course)
course.extend(['dev','i','am','devansh'])
print(course)
print(course[0:3])
print(course[-2])
course.insert(4,'not')
print(course)
print(dir(list))
course1=['bye','goodnight']
print(course1)
course.insert(0,course1)
print(course)
course.remove(['bye','goodnight'])
print('==========')
popped=course.pop(1)
print(popped)
print('==========')
course.sort()
#changes the original, so use sorted() instead ex: sorted(course)
print(course)
print('==========')
course.sort(reverse=True)
print(course)

nums=[1,2,3,4,5,6]
print(min(nums))
print(max(nums))
print(sum(nums))

print(course)
print(course.index('am'))

print('aert' in course)
i=0
for item in course:
    print(f'{(i+1)}th item is: {item}')
    i+=1

for index, item in enumerate(course):
    print(f'{index+1}th item is: {item}')

course_string=', '.join(course)
print(f'{course_string} {type(course_string)}')

string_to_list= course_string.split(', ')
print(string_to_list)

#tupples are not modifiable( immutable)

print('========')
tuple_1=('dev','i','am','devansh')
tuple_2=tuple_1

#tuple_1[0]='art' //error since immutable, no remove ,append, insert, only access, loop

#sets
#unordered and no duplicates

sets_1={'dev','dev','i','am','devansh'} #no duplicates
print(sets_1) #order of values can change everytime
#used in membership test to check if a value is part of a set
print('hello' in sets_1)
sets_2={'dev','dev','i','am','devansh','art','amath'}
print(sets_2.intersection(sets_1))
print(sets_2.difference(sets_1))
print(sets_1.union(sets_2))

#empty lists,sets,tuple

list1=[]
list1=list()

tuple3=()
tuple3=tuple()

empty_sets={} #wrong, its a dict
empty_sets=set()



#dict
#allow us to work with key value pairs, hash maps, associative arrays
#key- unique identifier
#value- corresponding data
student={'name':'devansh','rollno.':30,'age':19,'Course':["Cse(DS)",'Math']}
print(student)

print(student['Course'])
#course can be string, but no mutable
print(student.get('Phone','no key exists'))
student['Phone']=555555
print(student.get('Phone','no key exists'))
student['rollno.']=33
print(student)
student.update({'name':'Dev','Phone':'666555'})
print(student)
del student['Phone']
print(student)
popped=student.pop('age')
print(f'{popped} was popped')
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
for keys in student:
    print(keys)
for keys, values in student.items():
    print(keys, values)









