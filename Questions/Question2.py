#Write a function called capitalize. This function takes a string as an argument and capitalizes the first letter
# of each word. For example,
#'i like learning' becomes '1 Like Learning'.

import string
from string import capwords

string1='i like learning'
def capitalize(string1):
    string1=capwords(string1)
    print(string1)

capitalize(string1)