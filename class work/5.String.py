#string
Name="Hema"
print(type(Name))

#1.String Operations
#Concatenation(+)
fname='Pogaku'
lname='Hema'
print(fname+lname)

#Repetition(*)
name="Aswini"
print("Aswini"*4)

#Indexing
text="munibhargav"
print(text[3])
print(text[0])
print(text[-1])
print(text[-4])

#Slicing
name="SagarBabu"
print(name[0:6])
print(name[:4])
print(name[3:])
print(name[:])

#Membership
name='Hema'
print('Hema' in name)
print('latha'in name)
print('Hema' not in name)
print('Latha' not in name)

#2.String Functions
#len()
name="Hema"
print(len(name))

#max( and min()
name="EkshinXYZ"
print(min ("EkshinXYZ"))
print(max("EkshinXYZ"))

#Sorted()
name="Ekshin"
print(sorted("Ekshin"))

#chr() and ord()
x=('A')
print(ord(x))
x=('a')
print(ord(x))
x=('@')
print(ord(x))
#chr()   
print(chr(97))
print(chr(45))
print(chr(81))

#3.string case conversion methods
#upper case()
name="Hema"
print(name.upper())
#Lowercase()
name="EKSHIN"
print(name.lower())
#capitalizer()
name="Sandhya"
print(name.capitalize())
#title()
name="siddamma"
print(name.title())
#swapcase()
name="Rishikumar"
print(name.swapcase())
#casefold()
name= 'S'
print(name.casefold())

#4.Alignment & Formating Method
#Center()
name= 'Rishi'
print(name.center(20,'*'))
name= "chinnu"
print(name.center(20,"-"))
#ljust()
name="Aswini"
print(name.ljust(30,"^"))
#rjust()
name="strings"
print(name.rjust(20,"-"))
#Zfill()
a="933"
print(a.zfill(6))

#6.Search & Find Methods
#Find()
name="Baby"
print(name.find("a"))
name="kavya"
print(name.find("k"))
#rfind()
name="abcdabcdadc"
print(name.rfind("d"))
#index()
name="python"
print(name.index("t"))
print(name.index("o"))
#rindex()
name="abcabcabcabc"
print(name.rindex("c"))
print(name.rindex("a"))
#count()
name="pythoncourse"
print(name.count("o"))

#6.String Testing Methods
#starstwith()
name="21G21A04F1"
print(name.startswith("21"))
name="DS15"
print(name.startswith("DS"))
name="ABC123"
print(name.startswith("123"))
#endswith()
name="Hema"
print(name.endswith("ma"))
name="Harika"
print(name.endswith("Hari"))
#isalpha()
name="Hello"
print(name.isalpha())
name="ABC123"
print(name.isalpha())
#isalnum()
name="abc"
print(name.isalnum())
name="abc123"
print(name.isalnum())
name="@123"
print(name.isalnum())
#islower()
name="Hema"
print(name.islower())
name="HEMA"
print(name.islower())
#isupper()
name="YOUR FAV COLOUR"
print(name.isupper())
name="your fav colour"
print(name.isupper())
#isspace()
name="      "
print(name.isspace())
#istitle()
name="print hello"
print(name.istitle())
name="Print Hello"
print(name.istitle())
#isidentifier()
name="pythhon"
print(name.isidentifier())
name="@python"
print(name.isidentifier())

#7.Replace & Modify  Methods
#replace()
name="hasini hema"
print(name.replace("ma","s"))
#translate()
name="abc"
print(name.translate(str.maketrans("a","x")))
#maketrans()
name="python"
print(name.maketrans("th","#$"))

#8.Splitting & joining Methods
#split()
name="x,y,z"
print(name.split(","))
#rsplit()
name='u,v,x,y,z'
print(name.rsplit(",",1))
#splitlines()
name="hema\pogaku"
print(name.splitlines())
#join()
name="aswini priya"
print(",".join(name))
#partition()
name="python-course"
print(name.rpartition(","))
print(name.partition("-"))
name="python-course"
print(name.rpartition(","))
print(name.rpartition("-"))

#9.Whitespace & Trimming Methods
#Strip()
name="Lakshmi"
print(name.strip())
#lstrip()
name="-----laksmi"
print(name.lstrip("-"))
#rstrip()
name="lakshmi-----"
print(name.rstrip("-"))

#10. & Decoding Methods
#encode()
name="rishi"
print(name.encode())
#decode()
name=b'rishi'
print(name.decode())


