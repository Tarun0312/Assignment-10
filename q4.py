# 4. Write a python script to print first N odd natural numbers

N=int(input("Enter a number: "))

for i in range(1,2*N,2):
    print("%d"%i,end=' ')