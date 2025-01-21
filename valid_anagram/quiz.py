import random


def name():
    name = input("Enter your name: ")
    return name

def gets_number():
    count =0
    for i in range(10):
        num1 = random.randint(0,500)
        num2= random.randint(0,500)
        print(f"What is the answer to the following question: {num1} +{num2}")
        addition = int(input())
        if addition == num1+num2:
            print(f"The answer is correct: {num1+num2}")
            count+=1
        else:
            print("The answer is incorrect")
    print(f"The number of correct iterations: {count}")
    print(f"The average right is:{(count/10)*100}%")


print(f"the name of student is: {name()}")
print(f"The additions{gets_number()}")




