
# write a programm to print the multiplication table of the number entered by the user.
number=int(input("enter the number"))
i=1
while i<=10:
    print(i*number)
    i=i+1
# ask the user to enter 10 number using only one input statement and add them to the list

list=[]
for name in range(10):
    number=input("enter the number:")
    list.append(number)
    print(list)
else:
    print("that's all")

# from a list of numbers make a new list containing only the even numbers.

x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print("the value of x",x)
list=[]
for i in x:
   if i%2==0:
       list.append(i)
       print("even numbers are:",list)

# from a list separate the integer,string and floats elements into three different lists.
list=[1,"egg",2.50,5,"fish",3.9,6,"hen",6.9]
print("list:",list)
integer=[]
string_list=[]
float_value=[]
for i in list:

    if type(i)==str:
        string_list.append(i)

    if type(i)==int:
        integer.append(i)
    if type(i)==float:
        float_value.append(i)
print(integer)
print(string_list)
print(float_value)

# from a list ask the user the number he wants to remove from the list and then print the list.
list=[1,2,3,4,5,6,7,8,9,10]
print("list is",list)
n=int(input("enter the number want to remove from list"))
list.remove(n)
print("our new list",list)

# make a calculator

a=int(input("enter the number"))
b=int(input("enter the number"))
ch=input("a-Addition\n s-subtract\n m-multiplication\n d-division\n Q-quit")
while ch!='q':
    if ch=='a':
        print("the sum of two number is",a+b)
    if ch=='s':
        print("the subtract of two number is",a-b)
    if ch=='m':
        print("the multiplication of two number is",a*b)
    if ch=='d':
        print("the division of two number is",a/b)
    if ch=='Q':
        print("quit")
    ch=input("enter choice again\n a-Addition\n s-subtract\n m-multiplay\n d-division\n Q-quit")
