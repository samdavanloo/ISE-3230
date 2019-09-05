##### Basics #####

# Following codes are compatible with Python 3

#%%
# To comment use #
# To make a new section use #%%

#%%
### getting and setting current working directory and view their contents
import os # importing a module
os.getcwd()
os.chdir('/Users/Sam/Box/0-Sam/MyGitHub/ISE-3230')
os.getcwd()
os.listdir(os.getcwd()) #see the contenets of the current directory

#%%
myint=7 # type is integer
myfloat=7.0 # type is float
myfloat=7.
myfloat=float(7)
print(myint+myfloat)
myint/8
myfloat/8
import math   # import module
math.sqrt(36)
from math import sqrt   # from 'module' import 'objecte'
sqrt(36)
vol=3 # type integer
print(vol) # print needs ()
'hello world!'
x='hello' # type is string
x
print(x)
x,y=2,3 # multiple assignment
y,x
x=y=z=10
x,y,z
x=1; y=2
x, y
print('my volume is', vol)
phrase='hello '+'world' # concatenate strings
print(phrase)

#%% clearing console, deleting variable
clear() # clear console

y=1
z=2
del y, z # to remove variable(s), note that they should exist, otherwise error

# Removing all of the names ( variables)
import sys
sys.modules[__name__].__dict__.clear()

#%%
### Data Structures: [list], (tuple), {set}, {dictionary}

#%%
### 1. Lists [they are constructed by bracket]

# General purpose, most widely used data structure, sequence type, sortable, and mutable. 

cities=['NYC','LA','SF']
cities
type(cities)
cities[0] # index starts at 0 (known as slicing or subsetting)
cities[-1]
cities.append('CHI')
cities
new_list=['hello',2,'all',39.5] # don't need to have the same data type, but not recommended
new_list
len(new_list)

my_list=[1,2,3,4]
my_list2=my_list #dependent copy
my_list2
my_list[0]=10
my_list2
my_list3=my_list[:] #independent copy
my_list[1]=20
my_list3

# some operators
3 in my_list
[1,2,3]+[4,5,6]
[1,2,3]*3

# some methods
my_list=[1,2]
my_list.append(3)
my_list
my_list.insert(0,5) # where, what
my_list
my_list.extend([100,101])
my_list
my_list.index(5) # returns index of the argument (index starts at 0)

ages=[12,34,1,3]
ages.sort()
ages

#%%
### 2. Tuples (they are constructed by parantheses)

# Immutable (can't add or change), useful for fixed data, faster than lists, sequence type

my_tuple=(1,2,3)
my_tuple
my_tuple[0] # tuples are faster than lists (index starts at 0)
my_tuple=(23,14,22)
my_list=list(my_tuple) #switch btw. list and tuple
my_list
my_tuple2=tuple(my_list)
my_tuple2

#%%
### 3. Sets {defined using curly brackets}

# Store non-duplicated items, very fast access vs. lists, 
# math set operations (union, intersection), unordered

my_set={1,1,1,2,3,3}
my_set
len(my_set)
range(10) #result is a set
range(3,8) #upto 7
range(0,20,2)
3 in my_set  
4 not in my_set    
my_set1=my_set.copy() #independent copy
my_set2={3,3,3,4,5,5,6}
my_set2 #no duplicates
set.intersection(my_set1,my_set2)
set.union(my_set1,my_set2)
 
#%%                         
### 4. Dictionaries {they are constructed by curly brackets} -- key:value

# Key/Value pairs, associative arrays (like Java HashMap), unordered
# keys are immutable. Values could be of any type.

my_dict={'sam':33,'john':22,'edward':20}
my_dict
my_dict['sam']
len(my_dict)
my_dict2=my_dict.copy()  #independent copy
my_dict2

'john' in my_dict
my_dict.clear()
my_dict

#dictionar methods
my_dict={"foo":1,"bar":2}
my_dict.keys()
my_dict.values()
my_dict.items()

#%%
### miscellaneous
z=True #type boolean
z
type(z)

y=None #type is NoneType
y
type(y)

#%%
### logical operators, if/else, loops, etc. (indentations are important)

### If/else
x=0
y=4
if x==1 and y==3:
    print('first condition satisfied')
elif x==1 or y==3:
    print('second condition satisfied')
else:
    print('Neither condition satisfied')

###  some loops
cities=['NYC','LA','SF','CHI']
for city in cities:
    print(city)
    
for i in range(1,10):
    print('The inverse of ', i, 'is', 1.0/i)
    
for letter in 'Hello':
    print(letter)

for city in cities:
    if city=='NYC':
            print('Cool')
    elif city == 'SF': #notice the indentations
            print('still cool')
    else:   
            print('fine')

a = 10
while a > 0:
    print(a)
    a -= 1   # a=a-1 (similarly, we have a += 1)


num=2
for i in [1,2,3,4]:
    if i > num:
        break # exits the loop
    else:
        print(i)

#%%
###  defining functions  (are variables are local unless sepcified as global)
def adder(num1,num2):
    ### this function adds num1 to num2 ###
    ans=num1+num2
    return ans

adder(3,4)

