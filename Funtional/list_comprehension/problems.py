#1  1 to 1000 create elemts
#2  find all number  from 1 - 500  that are divible by  7
#3  find all of the numbers 1 - 300 that have 3 in them
#4  count number of spaces in a string
#5  Find total number of vowels in a string
#6  find all of the words in a string that are less than 4 letters

string='Practice list comprehension problems to drill your head'

# lst=[i for i in range(1,1001)]
# print(lst)

# lst=[i for i in range(1,300) if i%7==0]
# print(lst)

# lst=[i for i in range(1,301) if '3' in str(i)]
# print(lst)

# lst=len([i for i in string if i==' '])
# print(lst)


# vowels='aeiouAEIOU'
# lst=len([i for i in string if i not in vowels])
# print(lst)

data=string.split(' ')
lst=[i for i in data if len(i)<4]
print(lst)