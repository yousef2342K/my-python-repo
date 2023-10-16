def BinarySearch(array,query,lowestindex,highestindex):

    while lowestindex <= highestindex:
        mid = lowestindex + (highestindex-lowestindex)// 2  # to get the closer integer  
        if array[mid] == search:
            return mid
        elif array[mid] < search:
            lowestindex = mid + 1 
        else : 
            highestindex = mid - 1
    return -1

def sortjoe(my_list1):

    for index in range (0 , length - 1): # range (0,5) 
        for compare in range(0,length - index - 1): # range(0 , 5 - index) # index = 0 , 1 , 2 , 3 , 4
            first = my_list1[compare]
            second = my_list1[compare+1]
            if first > second:
                my_list1[compare] = second
                my_list1[compare+1] = first

my_list = [1,2,4,100,5,6]
search = 100
length = len(my_list)

my_list2 = sortjoe(my_list)
result = BinarySearch(my_list,search, 0 , length-1)

if result == -1:
    print("Element not found !")
else:
    print(f"found")
