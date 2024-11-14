string='luminar technolab'
vowels='aeiouAEIOU'
lst=[]
for i in string:
    if(i in vowels):
        lst.append(i)

print(len(lst))