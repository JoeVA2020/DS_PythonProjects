# Write a function that has one parameter and takes a list of words as an argument. The function returns the longest word from the list.
# Name the function longest word. The function should return the longest word and the number of letters in that word. For example, if you
# pass ['Java, 'JavaScript', 'Python'], your function should return [10, JavaScript] as the longest word.

def longest_word(words):
    longest=max(words,key=len)
    return print(len(longest),longest)

lst=['Java', 'JavaScript', 'Python']
words=lst
longest_word(words)