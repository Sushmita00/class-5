'''
print("1\n  2\n   3\n     4\n       5")

for x in range(1,1000000):
    print(x)


for x in range(1,10,2):
    print(x)
else:
    print("thats all")

i=0
while i<5:
    print(i)
    i=i+1

name=input("enter the name")
while name.isdigit()==True or len(name)<4:
    name=input("please enter the name")
print("Name accepted")
print("hello:",name)


name=input("enter the name")
if len(name)>3:
    print("valid")
else:
    print("invalid")
'''

a=10
if type(a)==int:
     print("it is an integer")



