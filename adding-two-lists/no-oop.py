""" Defining three lists and counter variable {n}  """

my_list = [1,2,0,4,5]
list2 = [5,6,7,8,0]
counter = 0
list3 = []

""" looping within the list """

for my_list[counter] in my_list:
    try:
        my_list[counter]
    except:
        my_list[counter]=0
    for list2[counter] in list2:
        x = my_list[counter]+list2[counter]
        list3.append(x)
        counter+=1

""" ending the loop ""

    if counter == len(my_list) and len(list2):
        break
''' Hehe the final result '''

print(f'{list3} is the sum of \n {my_list} and {list2}')
