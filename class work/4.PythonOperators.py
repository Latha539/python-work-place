a=40
b=50
print("Addition(+):",a+b)           #Addition(+): 90
print("Subtraction(-):",a-b)        #Subtraction(-): -10
print("Multiplication(*):",a*b)     #Multiplication(*): 2000  
print("Division(/):",a/b)           #Division(/): 0.8
print("Floor Division(//):",a//b)   #Floor Division(//): 0
print("Modulus(%):",a%b)            #Modulus(%): 40
print("exponentional(**):",a**b)    #exponentional(**): 126765060022822940149670320537600000000000000000000000000000000000000000000000000

#2.comparison operators               
print("equal to(==):",a==b)                 #equal to(==): False
print("Not Equal to(!=):",a!=b)             #Not Equal to(!=): True  
print("Greater than(>):",a>b)               #Greater than(>): False
print("Less than(<):",a<b)                  #Less than(<): True
print("Greater than or Equal to(>=):",a>=b) #Greater than or Equal to(>=): False              
print("lesser than or equal to(<=):",a<=b)  #lesser than or equal to(<=): True    

#3.Assignment Operators
a=2
print("Assign(=):",a)                        #Assign(=): 2  
a+=3
print("Addition & Assign(+=):",a)             #Addition & Assign(+=): 5 
a-=3
print("subtract & Assign(-=):",a)           #subtract & Assign(-=): 2
a*=2
print("Multiply & Assign(*=):",a)            #Multiply & Assign(*=): 4 
a/=3
print("Divide & Assign(/=):",a)             #Divide & Assign(/=): 1.3333333333333333  
a//=2
print("Floor Divide & Assign(//=):",a)      #Floor Divide & Assign(//=): 0.0
a%=3
print("Modulus & Assign(%=):",a)            #Modulus & Assign(%=): 0.0
a**=2
print("Exponentiate & Assign(**=):",a)      #Exponentiate & Assign(**=): 0.0

#Logical Operations
a=5
b=10
print("And:",a>b and b>a and a<b)          #And: False
print("And:",a%3==0 and b%5==0)            #And: False
print("or:",a%2==0 or b%2==0)              #or: True
print("Not:",not b%3==0)                   #Not: True

#Membership Operators
a = 'Hema'
print('a' in a)      #True
print('a' not in a)  #False
#list
N=["mounika","bhavana","srija","hema"]
print("srija" in N)        #True
print("mounika" not in N)  #False
print("mounika"in N)        #True
#tuple
t=(1,3,5,7)     
print( 1 in t)  #true
print(5 in t)   #True
print(5 not in t) #False
#set
s={1,2,3,4}
print(2 in s)      #Ture
print(5 not in s)  #Ture
print(5 in s)       #False
#dictionary
d={'Name':"Hema",'course':"Ds",'age':"21"}
print('Name' in d)  #Ture
print("21" in d)    #False
print('course' in d) #True
print('age' in d)    #True