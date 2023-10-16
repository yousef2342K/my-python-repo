my_list = [2 , 6 , 4 , 1 , 3 , 5] # size : 6  # => [1 , 2 , 3 , 4 , 5 , 6]
print(my_list)

# Bubble sort algorithm
# 1 - loop in the array by index len(my_list)-1
# compare every element with the next one

length = len(my_list) # print the length of the array (list)

print(length)


# loop on elements in the array


for index in range (0 , length - 1): # range (0,5) 
    for compare in range(0,length - index - 1): # range(0 , 5 - index) # index = 0 , 1 , 2 , 3 , 4
        first = my_list[compare]
        second = my_list[compare+1]
        if first > second:
            my_list[compare] = second
            my_list[compare+1] = first
        

print(my_list)
