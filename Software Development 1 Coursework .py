#!/usr/bin/env python
# coding: utf-8

# # Software Development 1 Courserwork

# In[54]:


#EXERCISE I
#1. Asks the user to enter a number “x” 
x = int (input ("10"))


# In[55]:


#2. Asks the user to enter a number "y"
y = int (input ("5"))


# In[56]:


print (x)


# In[57]:


print (y)


# In[58]:


#3a. The sum of x and y
print (x+y)


# In[59]:


#3b Asks the user to enter a number “y” 
print (x-y)


# In[60]:


#3c. The product of x and y 
print (x*y)


# In[61]:


#3d. The quotient when x is divided by y
print (x/y)


# In[62]:


#3e. The remainder when x is divided by y
print (x%y)


# In[63]:


#3f The result of log10x
import math #importin
print (math.log10(x))


# In[64]:


#3g The result of x**y
print (x**y)


# In[3]:


#EXERCISE II
#Write a program that asks the user to enter the width and length of a room in meters. Once these values have been
#read (as floating-point numbers), your program should compute and display the area of the room. Include units in your
#prompt and output message.

#Asking user to enter the width
width = float (input ('1.5'))
#Asking user to enter the length
length = float (input ("5.6"))
#To calcute the total of area, we will have to multiply the width by the length
#When the area is included in the print function then it multiplies and it's inlcuded in the result when we run 
#the cell 
area = width * length
print ("The total area of the room is", area, "meters")


# In[8]:


#EXERCISE III: CHINESE ZODIAC ASSIGNS 
year = int(input("Enter birth year: ")) #When we run the program it's going ask to enter the number of the year
#which will result to showing us the respective chinese zodiac sign. 
#The years are 2000 to 2011

#I will start the cycle with the year 1999 as it's when the previous cycle ended. 

zodiacYear = year % 12

if (zodiacYear %12 == 0): 
    print ("Hare")
elif (zodiacYear %12 == 1): 
    print ("Dragon")
elif (zodiacYear %12 == 2): 
    print ("Snake")
elif (zodiacYear %12 == 3):
    print ("Horse")
elif (zodiacYear %12 == 4):
    print ("Sheep")
elif (zodiacYear %12 == 5):
    print ("Monkey")
elif (zodiacYear %12 == 6): 
    print ("Rooster")
elif (zodiacYear %12 == 7): 
    print ("Pig")
elif (zodiacYear %12 == 8):
    print ("Rat")
elif (zodiacYear %12 == 9):
    print ("Ox")
elif (zodiacYear %12 == 10):
    print ("Tiger")
elif (zodiacYear %12 ==11):
    print ("Dog")
elif (zodiacYear %12 ==12):
    print ("Hare")

    #end
    


# In[5]:


#EXERCISE IV: MULTIPLICATION TABLE
#I will be using the def function, creating nested loops and asking the user to add a value and return it 
#in order to display the multiplication table. 

def nested_loop(start, end):
    # printing the top header
    print('', end='\t')
    for i in range(start, end +1):
        print(i, end='\t')
    print('')

    for i in range(start, end + 1):
        print(i, end='\t') # printing the running column 
        for j in range(start, end + 1):
            print(i * j, end='\t')
        print('')


def get_value(label):
    print("Enter " + label + " value:")
    value = int(input())
    return value # returning the calculation 


def table():
    start = get_value("starting")
    end = get_value("ending")
    nested_loop(start, end)

table ()

#To diplay multiplication table below, please run the code, add "1" as starting value and "10" as the ending value
#end


# In[1]:


#EXERCISE V - House Purchase Calculationsδ 

#Assigning values:

cost_of_home = 110000.0
down_payment = 110000.0 * 0.25 #110000.0 is the total cost of the future home times 25% (0.25)
#which I have turned into a float. 
annual_salary = 38000.0
portion_of_the_salary_saved = 0.1 #10% turned in decimals (float)
print ("The portion of the down payment is","£", down_payment)
savings= 0 
r = 0.04 

monthly_salary = (annual_salary / 12.0)
print (monthly_salary)

monthly_savings = monthly_salary*0.1 
print ("The monthly savings are", monthly_savings)



#Using the float function and the input function to ask the user for input of the following: 

cost_of_home = float (input("110000.0"))#Asking the user for input on the cost of my future home 

print ("The cost of the house is","£",cost_of_home ) #Printing a sentence that states the cost of the house

annual_salary = float (input (38000.0))#Asking the user for input of my starting annual salary. 
print ("My starting annual salary is","£", annual_salary) #Printing a sentence that states my annual salary. 

salary_saved = float (input (0.1)) #Asking the user for input of my saved salary 
print ("The portion of my salary saved is", salary_saved) #Printing a sentence that states my annual salary.



months = 0
# Want to exit the loop when there is enough savings for a down payment
while savings < down_payment:
    savings +=  savings * (0.4 / 12)  # Monthly interest
    savings += salary_saved  # Monthly savings
    months += 1
print("It will take {} months to save!".format(months))


