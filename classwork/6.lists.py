#Empty List 
l = [] #Empty list[]
l1 = list()#[]
print(1,11)

#List with Elements
l = [1,2,3,4,5] #List of integers
fruits = ["apple","banana","pappya"] #List of strings
n =[10, "python", 3.14, True] #mixed data type
print(1,fruits,n)

#List with Nestes Lists
n_1 = [[1, 2, 3],["a","b","c"],[True, False]]
print(n_1)

#List using list() construction
t_l = list((1,2,3)) # converting tuple to list
s_l = list("python") # ['p','y','t','n','o','n']
print(t_l,s_l)

#Accessing Elements in a List
print(l)
print(l[0]) #1
print(l[1]) #2
print(l[-1]) # 5(   Negative Indexing)
#slicing
print(l[1:4]) #[2,3,4]
print(l[:3]) #[1,2,3])(from start)
print(l[2:]) # [3,4,5] (to end)
print(l[::-1]) # [3,4]
print(l[::-1]) # [5,4,3,2,1](Reverse list)
#Changeing ele
l = [10, 20, 30, 40]
l[2] = 100
print(1)#[10, 20, 100, 40]

#Adding Elements
l. append(50) # Append (adds at to the end)
print(l)
l.insert(1, 15) # insert (adds to the end)
print(1) #[10, 15, 20, 100, 40]
l.extend([60, 70, 80]) # Extend (adds multiple elements)
print(l) #[10, 15, 20, 100, 40,50, 60,70, 80]

#Removing Elements
l.remove(100)#Removes first occurrence of 100
print(l) #[10, 20, 40, 50, 60, 70, 80]
l.pop(2) #Removes element at index 2
print(l) #[10, 15, 40, 50, 60, 70, 80]
l.pop() #Removes last element
print(l)  #[10, 15, 40, 50, 60, 70]
del l[1] #Deletes element at index 1
print(1) #[10, 40, 50, 60, 70]
l.clear() #clears the entire list
print(1)#[]

#List Methods
l = [10, 20, 30, 40, 20]
print(l.count(20)) # 2
print(l.index(40)) # 3
l.sort()#sort
print(l)  #[10, 20, 30, 40]
l.reverse() #reverse
print(l)   #[40,30,20,20,10]
l1 = l.copy() #copying
print(l1)#[40,30,20,20,10]

k = [20,10,30,40]
k.sort()   #sorting
print(k)   #[10, 20, 30, 40] 
print(sorted(k))  #[10, 20, 30, 40]
print(sorted(k))  #sorted [10, 20, 30, 40]
print(len(k))   #4
print(min(k))   #10
print(max(k))   #40     
print(sum(k))   #100     
print(any(k))   #Ture      
print(any(k))   #Ture   
print(all(k))   #True      
