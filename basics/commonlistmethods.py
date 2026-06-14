#unlike strings , lists are mutable
objects = ["Akash","orange",False,50.33]
print(objects)

#indexing
print(objects[0:])

#append - adds the element at the end of the list
objects.append(90)
print(objects)

#sort - sort out the numbers
list1 = [20,10,30,40]
list1.sort()
print(list1)

#insert - inserts the elements anywhere
objects.insert(2,"apple")
print(objects)

#remove - removes the element
objects.remove("orange")
print(objects)

#pop - removes the last element and return item
list1.pop()
print(list1)

#reverse - reverse the list
list1.reverse()
print(list1)

# count - counts the number of times elements are repeated
print(list1.count(20))

#extends - adds elements from another list
list1.extend(objects)
print(list1)

#clear - clear all the elements
list1.clear()
print(list1)
