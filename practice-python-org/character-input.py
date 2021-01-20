from datetime import date
import pdb

name = input("Your name: ")
age = int(input("Your age: "))
iterations = int(input("Display how many times: "))
years_till_100 = (100 - age) + int(date.today().year)

greeting_message = "Hi, " + name + ". You're currently " + str(age) + " years old.\n"

print(iterations * greeting_message)
print("You'll be 100 years old in the year: " + str(years_till_100))

# Examples
# print("Were" + "wolf")
# print("Door" + "man")
# print("4" + "chan")
# print(str(4) + "chan")
# print(4 * "test")
