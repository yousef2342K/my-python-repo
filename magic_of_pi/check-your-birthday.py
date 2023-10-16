""" I hope u find Your birthday in pi digits :) """
# Enjoy !


import os 

with open('pi_million_digits.txt') as file_object:

    contents = file_object.read()
print("Check if your birthday exists in pi digits")
retries = 0 
while retries < 5 :
    num_existed = input("Enter any birthday without - : ")

    if num_existed in contents:
        print("YES")
        retries+=1
    else: 
        print("No !")

    if retries == 5:
        print("End")
        
