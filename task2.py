#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
a = input("Enter first word: ")
b = input("Enter second word: ")
c = input("Enter third word: ")
d = input("Enter fourth word: ")
e = input("Enter fifth word: ")
list1 = []
list1.append(a)
list1.append(b)
list1.append(c)
list1.append(d)
list1.append(e)
print(list1)
