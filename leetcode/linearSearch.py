def linearSearch(array,query):
    for index in range(0 , len(array)):
        if array[index] == query:
            return array[index]
    return -1


my_list = [1,2,4,100,5,6]
search = 100
result = linearSearch(my_list,search)


if result == -1:
    print("Element not found !")
else:
    print(f"found")
