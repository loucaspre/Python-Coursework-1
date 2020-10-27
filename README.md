# Python-Coursework-1
This is my first coding exercise as an MSc Computing student at the university of Roehampton

I . Write a program that does the following in order:
1) Asks the user to enter a number “x”
2) Asks the user to enter a number “y”
3) Prints out:
a. The sum of x and y
b. The difference when y is subtracted from x
c. The product of x and y
d. The quotient when x is divided by y
e. The remainder when x is divided by y
f. The result of log10 x
g. The result of x y

```python
#EXERCISE I
#1. Asks the user to enter a number “x” 
x = int (input ("10"))
#2. Asks the user to enter a number "y"
y = int (input ("5"))
print (x)
print (y)
#3a. The sum of x and y
print (x+y)
#3b Asks the user to enter a number “y” 
print (x-y)
#3c. The product of x and y 
print (x*y)
#3d. The quotient when x is divided by y
print (x/y)
#3e. The remainder when x is divided by y
print (x%y)
#3e. The remainder when x is divided by y
print (x%y)
#3f The result of log10x
import math 
print (math.log10(x))
```
II . Write a program that asks the user to enter the width and length of a room in meters. Once these values have been
read (as floating-point numbers), your program should compute and display the area of the room. Include units in your
prompt and output message.
```python

#EXERCISE II
#Write a program that asks the user to enter the width and length of a room in meters. Once these values have been
#read (as floating-point numbers), your program should compute and display the area of the room.

```python

#Asking user to enter the width
width = float (input ('1.5'))
#Asking user to enter the length
length = float (input ("5.6"))
#To calcute the total of area, we will have to multiply the width by the length
#When the area is included in the print function then it multiplies and it's inlcuded in the result when we run 
#the cell 
area = width * length
print ("The total area of the room is", area, "meters")
```
III . The Chinese zodiac assigns animals to years in a 12-year cycle. One 12-year cycle is:
2000 - Dragon
2001 - Snake
2002 - Horse
2003 - Sheep
2004 - Monkey
2005 - Rooster
2006 - Pig
2007 - Rat
2008 - Ox
2009 - Tiger
2010 - Dog
2011 - Hare
The pattern repeats from there, with 2012 being another year of the dragon, and 1999 being another year of the hare.
Write a program that reads a year from the user and displays the animal associated with that year. Can you make it
work for any year greater than or equal to zero?

```python
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
```
IV. Create a program that displays a multiplication table that shows the products of all combinations of integers from 1
times 1 up to and including 10 times 10. Your multiplication table should include a row of labels across the top of it
containing the numbers 1 through 10. It should also include labels down the left side consisting of the numbers 1
through 10.

```python

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
```
V . You have graduated from Roehampton University and now have a great job based in London! You decide that you
are better off buying a house rather than renting a flat, so you want to start saving towards it. As housing prices are
very high in Zone 1 and 2, you realize you are going to have to save first for some time before you make the down
payment on a house. To figure out how long will it take you to save enough money for the down payment, as a software
developer, your first instinct should be to write a general python program that takes into account:

1. The cost of your ideal house. (basic)

2. The cost needed for a down payment. (basic)

3. Your annual salary. (basic)

4. The portion of your salary that you will save (intermediate)

5. The amount of money that you have already saved. (intermediate)

6. That you are able to invest your savings. Having an annual return of r means that at the end of each month, you
receive an additional (r/12) times your saved money (r is divided by 12; the 12 is because r is an annual rate).
(advanced)

Write a program that ask the user for input on:
a) The cost of your future home
b) The starting annual salary
c) The portion of salary to be saved
and calculates how many months it will take you to save up enough money for a down payment with the following
assumptions:
i. That you start savings of £0.00.

ii. The down payment is 25% of the house’s value.

iii. That you will save up to 10% of your salary each month.

iv. That your investments earn a return of r = 0.04 (4%), so at the end of each month, your savings will be increased
by the return on your investment, plus a percentage of your monthly salary.

Tip 1: You will want your main variables to be floats, so you should cast user inputs to floats.

Tip 2: You should decide what information you need. Be careful about values that represent annual amounts and those
that represent monthly amounts.

Tip 3: you can assume that users will enter valid input (e.g. they won’t enter a string when you expect an int) but
successfully handling invalid input will get you higher marks.
```python
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
```






