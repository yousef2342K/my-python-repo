def summation(x):
    result_1 = 0
    for j in range(1,x+1,1):
        if j % 2 == 0:
            result_1 -= 1/factorial(j)
        else:
            result_1 += 1/factorial(j)
    return result_1

def factorial(n):
    result = 1
    for i in range(1,n+1,1):
        result *= i
    return result
    

num = int(input("Enter the number you want to figure out its factorial fraction summation : "))

print("the result is " , summation(num))
