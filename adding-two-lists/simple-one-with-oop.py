""" Adding two lists with oop dependencies


Writing code in oop is more efficent than simple code with only functions   



"""


# Example == [1,2,3] + [2,3,0] == [3,5,3]


class Adder:

    def __init__(self, num1, num2):
        self.list1 = []
        self.list2 = []
        self.list3 = []
        self.num1 = num1
        self.num2 = num2
    
    def split_num(self):
        """ defining the two lists """
        for num in str(self.num1):
            self.list1.append(int(num))
        for num in str(self.num2):
            self.list2.append(int(num))

    def add_lists(self):
        """ Adding the two lists into one """
        max_len = max(len(self.list1), len(self.list2))
        for i in range(max_len):
            x = self.list1[i] if i < len(self.list1) else 0
            y = self.list2[i] if i < len(self.list2) else 0
            self.list3.append(x + y)

    def print_list(self):
        """ the function which prints the three lists """
        print(f"List 1: {self.list1}")
        print(f"List 2: {self.list2}")
        print(f"List 3: {self.list3} is the sum of {self.list1} and {self.list2}")

num1 = int(input("Enter a number of any number of digits: "))
num2 = int(input("Enter a number of any number of digits again: "))

adder = Adder(num1, num2)
adder.split_num()
adder.add_lists()
adder.print_list()
