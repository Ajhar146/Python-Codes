
print(1)                  
print("Hello World")

print(2)
#In Python, we don't need to initialize the data type of a variable. Python detects it automatically.(implicit)
age=23
name="azhar"
height=5.10
print(age)
print(name)
print(type(age))
print(type(name))
print(type(height))
print(type(3.0))   # class <float>
                   # type returns the data type of the variable
                   
print(3,"   : Expression Execution")                                                                                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
A,B=2,3
text="$"
print(2*text*3)  #in python String & numeric can operate together               
                   
a,b="2",4
txt="@"
print((a+txt)*b) # here we can add two string by using Plus sign(concaternation)

print(4,"   : integer Division")                  
A,B=4.5,2                   
c=A//B   # returns floor values
print(c,A/B)


# taking input frm user and printing it
print(5,"   : input ") 
name = input("name :")
age = int(input("age :"))
height=float(input("height :"))
print(" my Name is :", name, "\n I am :", age,"years Old", "\n my Height is :", height)


print("hello world")
# a**b=a^b