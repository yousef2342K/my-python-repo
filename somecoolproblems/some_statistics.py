my_list = [[1,4],[2,1],[4,1],[2,1],[2,9]]

sum = 0
counter = 0
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        sum+= my_list[i][j]
        counter+=1

mean = sum/counter   # calculate the mean of the numbers 
div = 0

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        div += (my_list[i][j]-mean)**2

variance """ for samples """  = div / (counter-1)  # calculate the variance of the numbers
variance """ for population """  = div / (counter)
std = variance**(1/2)  # calculate the standard deviation of the numbers

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        if my_list[i][j]< int(std):
            final_num = my_list[i][j]


# print(f"the variance of the numbers of the list is {std}")
        
