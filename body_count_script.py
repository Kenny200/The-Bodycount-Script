#program to check user age and their bodycount
import random
import sys
from datetime import datetime


user_age = 0
user_bdy_count = 0
user_bdy_weight = 0
isHoe = False
isAdult = False
cur_date = datetime.now().date().strftime("%d/%m/%Y")
birth_date = input("\nEnter your dob:")
chck_birth_date = birth_date.split("/")
chck_cur_date = cur_date.split("/")
chck_gap = int(chck_cur_date[2]) - int(chck_birth_date[2])

user_age = chck_gap
if user_age >= 18:
    isAdult = True
else:
    print("User is underage!")

user_gender = input("Enter your gender").lower()
match user_gender:
    case "male":
        print("Hello king!")
    case "female":
        print("Hello queen!")
    case "nonbinary":
        sys.exit("404: gender not found") 

user_bdy_count = int(input("\nEnter your bodycount:"))
user_bdy_weight = float(input("Enter your weight:"))
pick_conversion = input("American or foreign units?").lower()
def convert_weight(weight, unit):
    global user_bdy_weight
    if unit == "american".lower():
        user_bdy_weight = weight * 0.453592
        return user_bdy_weight
    elif unit == "foreign".lower():
        user_bdy_weight = weight * 2.20462
        return user_bdy_weight
    else:
        raise ValueError("Invalid unit. Please choose 'pounds' or 'foreign units'.") 
    
print(f'user_bdy_count: {user_bdy_count}')      
print(f'user_bdy_weight: {user_bdy_weight}')      

if user_bdy_count >= 5 and isAdult == False:
    print("Wowza, this early?")
    isHoe = True
if user_bdy_count >= 5 and isAdult == True:
    print("Wowza, at least you're a adult")
if user_bdy_count >= 5 and user_bdy_weight >= 200:
    print("How?")
if user_bdy_count >= 5 and user_bdy_weight >= 200 and isAdult == False:
    print("How? And you're underage? Someone call Dr. Phil!")
