# Code for making arrays of user choices
#OOP_MAKES_CODE_EASIER


class Array:
    def __init__(self):

      
        """Intialization of the arrayy"""

      
        self.my_list = []
    def array_collector(self):
      
        """Here i am getting the inputsss"""

      
        while True:
            try:
                num_needed = int(input("Enter Your num of rounds : "))
                break
            except ValueError:
                print("Enter a number for rounds!!")

        for i in range(1, num_needed + 1):
             
             """Looping"""

          
             while True:
                try:
                    nums_needed = int(input(f"Enter Your num {i} : "))
                    self.my_list.append(nums_needed)
                    break
             
                except ValueError:
                   print(f"Enter a number for num {i}!!")
        
array_1 = Array()
array_1.array_collector()

print(array_1.my_list)
