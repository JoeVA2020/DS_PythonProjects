# Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. For
# example, if you pass '23569' as an argument, your function should return 9. Use list comprehension

num='23569'
def biggest_odd(num):
    print(max([i for i in num]))

biggest_odd(num)