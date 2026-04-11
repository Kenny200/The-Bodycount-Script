#program to check user age and their bodycount
import random
from datetime import datetime

print(ascii_banner)

user_age = 0
user_bdy_count = 0
isHoe = False
isAdult = False
cur_date = datetime.now().date().strftime("%d/%m/%Y")
print(cur_date)


birth_date = input("\nEnter your dob:")
print(birth_date)

chck_birth_date = birth_date.split("/")
chck_cur_date = cur_date.split("/")
chck_gap = int(chck_cur_date[2]) - int(chck_birth_date[2])
print(chck_birth_date)

print(f'age = {chck_gap}')
user_age = chck_gap
if user_age >= 18:
    isAdult = True
else:
    print("User is underage!")

user_bdy_count = input("\nWhat is your bodycount?")
if user_bdy_count >= 5 and isAdult == False:
    print("Wowza, this early?")
    isHoe = True
