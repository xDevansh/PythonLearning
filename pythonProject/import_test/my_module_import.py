import my_module as mm
import sys
import random
import datetime
import os
import calendar
#if not found or somewhere else then add the path to sys.path by using append() much better is by adding the folder to environment path variable "PYTHONPATH"
#or from my_module import find_index as fi ///from __ import *
#it checks for the module in various paths mentioned in sys.paths
courses= ['math','art','science','history','geography']

print('enter the target which you wanna find in the courses list')
target= input()
index= mm.find_index(courses,target)
if index==-1:
    print('not found in courses list')
else:
    print(f'found at index={index}')

print(sys.path)
random_choice= random.choice(courses)
print(random_choice)
print(datetime.date.today())
print(mm.__file__) #dunder file shows path