numbers = [2,6,4,9,7,5]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(5)
print(numbers)
numbers.insert(3,2) #1st the index where you want to insert. 2nd the number to insert
print(numbers)
print(numbers.count(2))
print(numbers[1:5]) #slicing doesn't change the original list unlike sort and reverse
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers.remove(4)
print(numbers)
numbers.pop() #removes the last element from the list
print(numbers)

#Mutable-Values can change. Ex:Lists
#Immutable-Values cannot change Ex:Tuples

#To create a single element tuple add a ',' after the element
tp=(1,)
print(tp)
