#QUESTION 1
# lst=[15,20,25,30,35,40,50]
# print(lst[-2]+lst[-0]+lst[1])
#Ans: 75  Negetive 0 is 0

#QUESTION 2
#Convert lst=[15,3,10,6,9,7] to [35, 47, 40, 44, 41, 43]
# lst=[15,3,10,6,9,7]
# lst_sum=sum(lst)
# lst2=[]
# for i in lst:
#     lst2.append(lst_sum-i)
# print(lst2)

#QUESTION 3
# lst=[1,3,4,5,8,6,5,3,2,4,6,8,9,7,5,4,8,9,12]
# #lst1=[1,8,2,9,4]
# lst1=[]
# for i in range(0,len(lst)-1):
#     if (lst[i-1]<lst[i]>lst[i+1] or lst[i-1]>lst[i]<lst[i+1]):
#         lst1.append(lst[i])
# print(lst1)

import itertools
import string

def generate_identifiers(n):
    if n <= 0:
        return []

    # Define character sets
    initial_chars = string.ascii_letters + "_"
    valid_chars = string.ascii_letters + string.digits + "_"

    # Generate identifiers of length n
    identifiers = []
    for initial in initial_chars:
        if n == 1:
            identifiers.append(initial)
        else:
            for chars in itertools.product(valid_chars, repeat=n-1):
                identifiers.append(initial + ''.join(chars))

    return identifiers

def main():
    try:
        n = int(input("Enter the length of the identifiers: "))
        if n <= 0:
            print("Length must be a positive integer.")
            return

        identifiers = generate_identifiers(n)
        print(f"Total identifiers generated: {len(identifiers)}")
        print("Sample identifiers (showing first 10):")
        print(identifiers[:10])
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

