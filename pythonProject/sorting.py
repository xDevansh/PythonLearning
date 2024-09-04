li=[9,1,2,5,6,8,4,7]
s_li=sorted(li)
print(f'sorted list: {s_li}')
print(f'original list: {li}')

li.sort()#returns none , sorts the original also to reverse pass reverse=True
print(li)

"""
tuple
"""
tup=(9,1,2,5,6,8,4,7)
#tup.sort() doesnt work
s_tup=sorted(tup) #a list
print(f"sorted tuple: {s_tup}")

"""dict"""
di={'name':'devansh','age':195}
s_di=sorted(di)
print(f"sorted dict: {s_di}")

"""sorting wrt abs"""
li1=[-4,2,-3,8,1,-6]
s_li1=sorted(li, key=abs)
print(s_li1)

"""
sorting objects wrt keys
"""
"""
using custom sort fn, using lambda fn inside key attribute, using attrgettr in operators module
"""
from operator import attrgetter
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __repr__(self):
        return '({},{},{})'.format(self.name,self.age,self.salary)

e1=Employee('Dev',19,70000)
e2=Employee('Raj',25,7000)
e3=Employee('ronak',22,80000)
employees =[e1,e2,e3]

#using custom sort fn
"""
def e_sort(emp):
    return emp.name
"""

s_employees=sorted(employees, key=lambda e:e.age) #used lambda fn to imitate the e_sort fn couldve passed e_sort in key instead
print(s_employees)
#couldve also used attrgetter by passing attrgetter(name) to key
#couldve also used attrgetter by passing attrgetter(name) to key


