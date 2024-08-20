
# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

language='python'
if language=='python':
    print("conditional was true")

if True:
    print('conditional is true')
print('====================')
l1=[1,2,3,4]
l2=[1,2,3,4]
print("when assigning same values to l1 l2 seperately")
if l1==l2:
    print('they are equal using ==')
if l2 is l1:
    print('object identity same')
else:
    print('object identity not same')
print('====================')
print('when assigning value of l1 to l2')
l1=[1,2,3,4]
l2=l1

if l1==l2:
    print('they are equal using ==')
if l2 is l1:
    print('object identity same')
else:
    print('object identity not same')
print('====================')
print("is the user admin?")
user=str(input())
print('is the user logged in?')
logged_in= str(input())
if user=='admin' and logged_in=='true':
    print('Admin is logged in')
elif user!='admin' and logged_in=='true':
    print('Non-Admin user logged-in')
else:
    print('unable to comprehend login credential and state')