from datetime import date


print("Hello, Welcome to welcome~")

name = input("Please input your name: ")
bday = int(input("Enter the year you birth: "))

todays_date = date.today()
year = todays_date.year

print("Your Name: " + name + "\nYour Age: " + str(year - bday))