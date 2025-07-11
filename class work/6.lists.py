#Empty List 
l = []
l1 = list()
print(1,11)

#List with Elements
l = [1,2,3,4,5]
fruits = ["apple","banana","pappya"]
n =[10, "python", 3.14, True]
print(1,fruits,n)

#List with Nestes Lists
n_1 = [[1, 2, 3],["a","b","c"],[True, False]]
print(n_1)

#List using list() construction
t_l = list((1,2,3))
s_l = list("python")
print(t_l,s_l)

#Accessing Elements in a List
print(l)
print(l[0])
print(l[1])
print(l[-1])
#slicing
print(l[1:4])
print(l[:3])
print(l[2:])
print(l[::-1])
print(l[::-1])
#Changeing ele
l = [10, 20, 30, 40]
l[2] = 100
print(1)

#Adding Elements
l. append(50)
print(l)
l.insert(1, 15)
print(1)
l.extend([60, 70, 80])
print(l)

#Removing Elements
l.remove(100)
print(l)
l.pop(2)
print(l)
l.pop()
print(l)
del l[1]
print(1)
l.clear()
print(1)

#List Methods
l = [10, 20, 30, 40, 20]
print(l.count(20))
print(l.index(40))
l.sort()
print(l)
l.reverse()
print(l)
l1 = l.copy()
print(l1)

k = [20,10,30,40]
k.sort()
print(k)
print(sorted(k))
print(len(k))
print(min(k))
print(max(k))        
print(sum(k))        
print(any(k))         
print(any(k))      
print(all(k))         
