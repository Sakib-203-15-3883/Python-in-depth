# list example in detail
list = ["sakib", 10 , "mukit", True , "talha", False  ]
print(list)

#accessing list item 
print(list[2])

# Slicing the elements 
list2 = list[1:4]
print(list2)
list2 = list[:4]
print(list2)
list2 = list[3:]
print(list2)
print(type(list2))

# negative indexing example 

list2 = list[-1]
print(list2) #False
list2 = list[-1 : -4]
print(list2)      #empty
list2 = list[-6 : -4] 
print(list2)     # "sakib", 10 


# updating list values 

list[1] = 15
print(list)


##########  Python List Operations   ############

# 1. Repetition operator(*)
list2 =   list * 2 
print(list2)

# 2. Concatenation operator(+)

list3 = list + list2
print(list3)

# 3. length  len()

print(len(list))

# 4. Iteration

for item in list :
  print(item)

print(item)

# 5. Membership(It returns true if a particular item exists in a particular list otherwise false.)

print(  "talha" in list )


# 6. Adding & Removing  Elements to the List [ Add an Element to the End of the List: append()], extend() Extend a List with Another Iterable,insert()  Insert an Element at a Specific Index, remove()  Remove the First Occurrence of a Value,pop() - Remove and Return an Element by Index (or the Last Element if not specified),  index() - Find the Index of the First Occurrence of a Value, sort() - Sort the List in Place , reverse() - Reverse the Elements of the List in Place , clear() - Remove All Items from the List, remove(),max(), min()

# Initial list
my_list = [4, 2, 8, 1, 7]

# Add an element to the end of the list: append()
my_list.append(5)
print("After appending 5:", my_list)

# Extend a list with another iterable: extend()
additional_elements = [9, 6]
my_list.extend(additional_elements)
print("After extending with [9, 6]:", my_list)

# Insert an element at a specific index: insert()
my_list.insert(2, 10)  # Insert 10 at index 2
print("After inserting 10 at index 2:", my_list)

# Remove the first occurrence of a value: remove()
my_list.remove(8)  # Remove the first occurrence of 8
print("After removing the first occurrence of 8:", my_list)

# Remove and return an element by index (or the last element if not specified): pop()
popped_element = my_list.pop(3)  # Remove and return the element at index 3
print("Popped element:", popped_element)
print("After popping the element at index 3:", my_list)

# Find the index of the first occurrence of a value: index()
index_of_7 = my_list.index(7)
print("Index of the first occurrence of 7:", index_of_7)

# Sort the list in place: sort()
my_list.sort()
print("After sorting:", my_list)

# Reverse the elements of the list in place: reverse()
my_list.reverse()
print("After reversing:", my_list)

# Remove all items from the list: clear()
my_list.clear()
print("After clearing the list:", my_list)
