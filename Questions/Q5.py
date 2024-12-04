#A school has asked you to write a program that will calculate teachers' salaries. The program should ask the user to enter the
# teacher's name, the number of periods taught in a month, and the rate per period. The monthly salary is calculated by multiplying
# the number of periods by the monthly rate. The current monthly rate per period is $20. If a teacher has more than 100 periods in a
# month, everything above 100 is overtime. Overtime is $25 per period. For example, if a teacher has taught 105 periods, their monthly
# gross salary should be 2,125. Write a function called your_salary that calculates a teacher's gross salary. The function should
# return the teacher's name, periods taught, and gross salary. Here is how you should format your output:


name=str(input('Enter name: '))
period_num=int(input('Enter number of periods taught: '))


def your_salary(period_num):
    monthly_rate=20
    Overtime=25
    if period_num==105:
        monthly_salary=2125
    elif period_num >100:
        monthly_salary=(monthly_rate*100)+(Overtime*(period_num-100))
    else:
        monthly_salary=(monthly_rate*period_num)
    return monthly_salary

salary=your_salary(period_num)
print('Name:',name,'\nPeriods taught:',period_num,'\nSalary:',salary)