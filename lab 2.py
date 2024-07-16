#while loop:
count=0
while(count<5):
    count=count+1
    print("Hello Warasat Ali")
    
#single staetment while block:
count==0
while(count==0):
 print("Hello Berlin")
print("Hello Professor")
 
#iterating over a list:
print("List iteration")
l=["Ariana","Brookfield","Smith"]
for i in l:
    print(i)

#iterating over a tuple:
print("\nTuple iteration")
t=("Ariana","Brookfield","Smith")
for i in t:
    print(i)
    
#iterating over a string:
print("\nString iteration")
s="Jason"
for i in s:
    print(i)
    
#iterating by index
list=["Ariana","Brookfield","Smith"]
for index in range(len(list)):
    print (list[index])
#except 'e' and 's':
for letter in 'geeksforgeeks':
    if letter=='e' or letter=='s':
        continue
    print ('current letter:', letter)
    var =10
    
#break it sees 'e' and 's':
for letter in 'geeksforgeeks':
    if letter=='e' or letter=='s':
        break
    print ('\ncurrent letter for break:', letter)

#creating a fuction:
    def my_function():
        print("hello function")
        
#calling a function:
    def my_function():
        print("hello function")
    my_function()
    
#calling a function by parameter:
    def my_function(fname):
        print(fname + " function")
    my_function("Email")
              
#default parameter value:
    def my_function(country="Norway"):
        print("I am from " + country)
    my_function("pakistan.")
    
#default parameter value:
    def my_function(country="Norway"):
        print("I am from " + country)
    my_function("pakistan.")    
#passing a list as a parameter:
    def my_function(food):
        for x in food:
         print(x)
    fruits=["apple","cherry"]
    my_function(fruits)
    
#return values:
    def my_function(x):
        return 5*x
    print (my_function(3))
    
#keywords arguments:
    def my_function(child3,child2,child1):
      print("The younguest child is " + child3)
    my_function(child1="lina",child2="rahim",child3="ania")
    
#create a class:
    class MyClass:x=5
    print("class in created")
#create object:
    p1=MyClass()
    print(p1.x)
    
#assign name and age:
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1=person("ania",12)
print (p1.name)
print (p1.age)
  
#object method:
class person:
  def __init__(self, name, age):
    self.name=name
    self.age=age
  def myfunction(self):
    print ("hello my name is " + self.name)
p1=person("ania",12)
p1.myfunction()


