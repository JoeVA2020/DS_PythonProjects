# Write two functions. The first function is called count_ words which takes a string of words and counts how many words are in
# the string.The second function called count_elements takes a string of words and counts how many elements are in the string. Do
# not count the whitespaces. The first function will return the number of words in a string and the second one will return the number
# of elements (less whitespace). If you pass 'I love learning', the count_words function should return 3 words and count_elements should
# return 13 elements.

def count_words(string):
    return len(string.split())

def count_elements(string):
    lst=[i for i in string if i !=' ']
    return len(lst)
string='hello my name is joe'
ans=count_words(string)
print(ans)
ans=count_elements(string)
print(ans)