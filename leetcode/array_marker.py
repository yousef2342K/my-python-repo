my_list = []
def main():
   num_needed = int(input("Enter Your num or rounds  : "))

   for i in range(1,num_needed+1,1):
       nums_needed = int(input(f"Enter Your num {i} : "))
       my_list.append(nums_needed)

main()
print(my_list)
