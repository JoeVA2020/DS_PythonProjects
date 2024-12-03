str='luminar_technolab'
vowels='aeiouAEIOU'
# lst=[i for i in str if i in vowels]
# print(len(lst))
#
# # OR
# lst=len([i for i in str if i in vowels])
# print(lst)

#``````````````````````````````````````````````````````````````````
#   CONSONENTS

lst=len([i for i in str if i not in vowels])
print(lst)