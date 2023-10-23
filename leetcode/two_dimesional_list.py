#nested list
# two dimensional array (list)
# list can take different data types but arrat does not
my_list = [[1,2,3],
           [5,6,7],
           [1,2,3]]


"""Looping in two dimensional array (list)"""
for i in range(len(my_list)):
    for j in range(len(my_list[i])):   
        if  i == j :
            print(my_list[i][j])

print(len(my_list))  # The length of the biggest array is 3 
print(len(my_list[i])) # the length of the smallest array is 3 


"""Looping in two dimensional array (list) but a bit easier"""
# for i in range(len(my_list)):
#     print(my_list[i][i])
