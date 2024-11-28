#Write a function called sort_words that takes a string of words as an argument, removes the whitespaces,
# and returns a list of letters sorted in alphabetical order. Letters will be separated by commas. All letters should
# appear once in the list. This means that you sort and remove duplicates. For example 'love life' should return as
# ['e,f,i,l,o,v'].

string=str(input('Enter string: '))
def sort_words(string):
    lst=[]
    for i in string:
        if(i not in lst) and (i != ' '):
            lst.append(i)
    lst.sort()
    print(lst)
    sortedlst=[','.join(lst)]
    print(sortedlst)

sort_words(string)
