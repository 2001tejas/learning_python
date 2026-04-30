# List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:

# list = ["i", "am", "tejas"]
# print(list)

# ['i', 'am', 'tejas']

# List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

# Note: There are some list methods that will change the order, but in general: the order of the items will not change.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

# lists = ["a", "b", "a"]
# print(lists)
# ['a', 'b', 'a']

# List Length
# To determine how many items a list has, use the len() function:

    # lists = ["a", "b", "a"]
    # print(len(lists)) #3

# List Items - Data Types
# List items can be of any data type:

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':

# lists = ["a", "b", "a"]
# print(type(lists)) #<class 'list'>

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

# Using the list() constructor to make a List:

# thislists = list(("a", "b", "c"))
# print(thislists)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Access Items
# List items are indexed and you can access them by referring to the index number:

# thislists = list(("a", "b", "c"))
# print(thislists[1]) #b

# Negative Indexing
# Negative indexing means start from the end

# -1 refers to the last item, -2 refers to the second last item etc.

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

# thislists = list(("a", "b", "c","d"))
# print(thislists[1:3]) #['b', 'c']

# Note: The search will start at index 2 (included) and end at index 3 (not included).

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:

# thislists = list(("a", "b", "c","d"))
# print(thislists[-3:-1]) #['b', 'c']

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:


# thislists = list(("a", "b", "c","d"))
# if "a" in thislists:
#  print("yes") #yes

# Change Item Value
# To change the value of a specific item, refer to the index number:

# thislists = list(("a", "b", "c","d"))
# thislists[3] = "e"
# print(thislists) #['a', 'b', 'c', 'e']


# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist.insert(2, "dragonfruit")
# print(thislist) #['apple', 'banana', 'dragonfruit', 'cherry', 'orange', 'kiwi', 'mango']

# Append Items
# To add an item to the end of the list, use the append() method:

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist.append("chikko")
# print(thislist) #['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango', 'chikko']

# Extend List
# To append elements from another list to the current list, use the extend() method.

# list_1 = ["i", "am"]
# list_2 = ["tejas"]
# list_1.extend(list_2)
# print(list_1) #['i', 'am', 'tejas']

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# Remove Specified Item
# The remove() method removes the specified item.

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:

# Remove Specified Index
# The pop() method removes the specified index.

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(2)
# print(thislist) #['apple', 'banana']

# If you do not specify the index, the pop() method removes the last item.

# The del keyword also removes the specified index:
# Remove the first item:

# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)

# The del keyword can also delete the list completely.
# thislist = ["apple", "banana", "cherry"]
# del thislist

# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.

# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist) #[]

# Loop Through a List
# You can loop through the list items by using a for loop:

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x) 

# apple
# banana
# cherry

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

# thislist = ["apple", "banana", "cherry"]
# for x in range(len(thislist)):
#     print(thislist[x])

# apple
# banana
# cherry

# Using a While Loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

# thislist = ["apple", "banana", "cherry", "chikko"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i+=1

# apple
# banana
# cherry
# chikko

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
#     A short hand for loop that will print all items in a list:

# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:
    
#     fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)  

# With list comprehension you can do all that with only one line of code:

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist) #['apple', 'banana', 'mango']

# newlist = [expression for item in iterable if condition == True]    
# The return value is a new list, leaving the old list unchanged.

# Condition
# The condition is like a filter that only accepts the items that evaluate to True.

# newlist = [x for x in fruits if x != "apple"]

# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

# The condition is optional and can be omitted:

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.

# newlist = [x for x in range(10)]

# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# newlist = [x.upper() for x in fruits]

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# fruits = [ "banana", "cherry","mango", "kiwi", "apple"]
# fruits.sort()
# print(fruits) #['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Sort Descending
# To sort descending, use the keyword argument reverse = True:

# num = [1, 3, 5, 6, 8, 4]
# num.sort(reverse=True)
# print(num) #[8, 6, 5, 4, 3, 1]

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Luckily we can use built-in functions as key functions when sorting a list.

# So if you want a case-insensitive sort function, use str.lower as a key function:

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# Use the copy() method
# You can use the built-in List method copy() to copy a list.

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# list = thislist.copy()
# print(list) #['banana', 'Orange', 'Kiwi', 'cherry']

# Use the list() method
# Another way to make a copy is to use the built-in method list().

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# list = list(thislist)
# print(list) #['banana', 'Orange', 'Kiwi', 'cherry']

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# list = thislist[:]
# print(list) #['banana', 'Orange', 'Kiwi', 'cherry']

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:

# Use the extend() method to add list2 at the end of list1:

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist)