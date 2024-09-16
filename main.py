#Determine the number is even or odd
num = int(input("Enter num: "))
if num % 2 == 0:
    print(f"The number {num} is Even!")
else:
    print(f"The number {num} is Odd!")
#Determine if the number is less than, equal to,or greater than zero
num=int(input("Enter a number:"))
if num<0:
    print("Number{num}is less than to zero")
if num>0:
    print("Number{num}is greater than to zero")
if num==0:
    print("Number{num}is equal to zero")
#Chek if the numbe is divicible by three
num=int(input("Enter a number:"))
if num%2==0 and num%3==0:
    if num%2==0:
     print("Number is devisible by 2")
    elif num%3==0:
        print("Number is devisible by 3")
else:
    print("Number is not devisible by 2 or 3")
#Detrmine voter eligibility based on the age and nationality
age=int(input("Enter your age:"))
nationality=str(input("Enter your nationality:"))
if age>=18:
    if nationality=="pakistani":
       print("You are eligible for vote")
else:
    print("Please obtain a valid id for vote")
#Categorize age into different life stages
age = int(input("Enter the age: "))
if 0 < age <= 12:
    print("You are a child")
elif 13 <= age <= 19:
    print("You are a teenager!")
elif 20 <= age <= 59:
    print("You are an adult!")
elif age >= 60:
    if age > 98:
        print("You are a dead man 😂!")
    else:
        print("You are a Senior citizen!")
elif age < 0:
    print("Invalid age")
else:
    print("Wrong age")
#Display the name of month based on the month number
month_number = int(input("Enter the month number: "))
if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")
elif month_number <= 0:
    print("Month number can't be negative!")
else:
    print("Only 12 months exist!")
#Chek if the year is leap or not
year = int(input("Enter the year: "))

if year % 4 == 0:
    print("Yes,{year} is a leap year")
else:
    print("The{year} is not a leap year")
