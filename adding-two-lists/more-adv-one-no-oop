
# this code without using oop or even functions
# just simple code 
# enjoy!!

list1 = []
list2 = []
num1 = int(input("Enter a number of any number of digits: "))
num2 = int(input("Enter a number of any number of digits again: "))

""" Looping part 1 """

for num3 in str(num1):
    list1.append(int(num3))
    
for num4 in str(num2):
    list2.append(int(num4))
    
""" Showing the two lists """

print(f'list 1 is {list1}')
print(f'list 2 is {list2}')

""" Defining new variables """

list3 = []
max_len = max(len(list1), len(list2))

""" looping num 2 """

for i in range(max_len):
    x = list1[i] if i < len(list1) else 0
    y = list2[i] if i < len(list2) else 0
    z = x + y
    list3.append(z)
""" final result """
print(f'{list3} is sum of {list1} and {list2}')
