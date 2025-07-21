#1 .sets
# creating aset with elements
my_set = {1, 2, 3, 4}
# set with duplicate elements
set = {1, 2, 3, 4}
print(set) # output: {1, 2, 3, 4}

#2 .operations on sets
#membership Testing
set = {1, 2, 3, 4}
print(3 in set) 
print(5 not in set)

#union()or union (l) method
sl={1,2,3}
s2={3,4,5}
result=sl|s2
print(result)

#(Intersection or &)
setl= {2,3,4}
set2= {4,5,6}
result= setl & set2
print(result)

#(difference or "-")
sl={2,4,6}
s2={6,8,9}
result= sl - s2
print(result)

#(symmetric Difference or ^)
sl={1,3,5}
s2={5,7,9}
result= sl ^ s2 
print(result)

#Subset (<= or issubset() method)
al={1,2}
a2={1,2,3}
print(al <= a2)

#Superset (>= or issuperset() method )
a1={1,2,3}
a2={1,2}
print(a1 >= a2)

#Disjoint sets (isdisjoint() method)
a1={1,2,3}
a2={4,5,6}
print(a1.isdisjoint(a2))

#3.sets methods
b1= {1,2,3,4}
b2={5,6,7,8}
#add
b1.add(5)
print(b1)
#remove
b1.discard(2)
print(b1)
#Discard
b1.discard(2)
print(b1)
#pop
b1.pop()
print(b1)
#clear
b2.clear
print(b2)
#Update
b1= {1,2,3,4}
b2={5,6,7,8}
b1.update(b2)
print(b1)

#intersection_update
names1= {'Ekshin','moshagna','rishi','srinu','mahi'}
names2={'rani','sitha','ramu','sunny','sai'}
names1.intersection_update(names2)
print(names1)

#difference_update
namesl= {'annu','ashok','sravani','sandhya'}
names2={'rishi','srinu','sunny','sagar'}
namesl.difference_update(names2)
print(names1)

#symmetric_difference_update
namesl={'safna','bhavana','mounika','harika'}
names2={'mounika','nani','chinni','sweety'}
namesl.symmetric_difference_update(names2)
print(namesl)


#copy()
fruits={'banana','pappya','apple','cherry'}
animals={'cat','dog','lion'}
food=fruits.copy()
print(food)

#Function for set
cl={3,5,7}
#len
print(len(cl))
print(cl)
#max
print(max(cl))
print(cl)
#min
print(min(cl))
print(cl)
#sum
c3={1,2,3,4}
print(sum(c3))
print(c3)
#sorted
c4={'classwork'}
print(sorted(c4))
print(cl)

#creating a frozenset
frozen = frozenset([1, 2, 3])
print(frozen) #{1,2,3}
# Frozenset is immutable
# The following will raise an error
# frozen.add(4)