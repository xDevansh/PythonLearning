month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """Return True for leap years"""
    if (year%4==0) and (year%400==0 or year%100!=0):
        print(f'Your provided year is a leap year:{year}')
    else:
        print(f'{year} is not a leap year.')
    return (year%4==0) and (year%400==0 or year%100!=0)

def days_in_month(year,month):
    if not 1<=month<=12:
        print('invalid month number')
        return
    if month==2 and is_leap(year):
        print("number of days is 29")
        return
    print(f'number of days is {month_days[month]}')

print("enter the year")
yr=int(input())
print('enter the month number')
mth=int(input())
days_in_month(yr,mth)