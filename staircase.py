# Author - anupama rajaram
# description - write a program that takes an integer input and creates a staircase.
#             example, if input = 3 then output as below
#               #
#              ##
#             ###


# initialize variables
i = 0
temp = 0
num = 0
n = []

# take input
n = input("Enter length of array; ")
num = int(n[0])


if(num < 1 or num>100):
    print("Invalid input. only accepting integers between 1 and 100.")
else:
    for i in range(1, num+1):
        temp = num-i
        print((" "*temp) + ("#"*i))
