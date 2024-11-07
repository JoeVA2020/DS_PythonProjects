
# read 6 inputs
# 1 current year
# 2 current month
# 3 current date
# 4 birth year
# 5 birth month
# 7 Birth date
# print Age

current_year=int(input("Enter current year: "))
current_month=int(input("Enter current month: "))
current_date=int(input("Enter current date: "))

birth_year=int(input("Enter birth Year: "))
birth_month=int(input("Enter birth month: "))
birth_date=int(input("Enter birth date: "))

age=current_year-birth_year

if(current_month<birth_month):
    age-=1
else:
    if(current_month==birth_month):
        if(current_date<birth_date):
            age-=1

print("Your age is:",age)