
# ******************************
# Make your Code
import random

numbers1 = []
numbers2 = []
sumList = []

for i in range(10):
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    numSum = num1 + num2

    numbers1.append(num1)
    numbers2.append(num2)
    sumList.append(numSum)

print(sumList)





