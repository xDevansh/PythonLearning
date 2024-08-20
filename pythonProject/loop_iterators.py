
nums=[1,2,3,4,5]
for num in nums:
    print(num)
print('=====')
for i in range(1,6,4): #stop,start,step (ex. if start from 3 with step 7 then next num=3+7
    print(i)
print('=====')

for i in range(10):
    if i==5:
        print(f'{i} Found!')
        break
    print(i)
print('=====')

for i in range(5):
    if i==3:
        print(f'{i} ignored')
        continue
    print('pls dont ignore me')

for idx, i in enumerate(nums):
    print(idx, i)

#while loop
x=0
while True:
    if x==5:
        break
    print(x)
    x+=1


while True:
    print('give a random number between 1 and 3')
    x=int(input())
    if x==1:
        print('congrats! loop breaked')
        break
    elif x==2 or x==3:
        print('badluck!')
    else:
        print('enter a valid number')

