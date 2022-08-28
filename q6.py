# 6. Write a python script to print first N even natural numbers

N=int(input("Enter a number: "))

for i in range(2,2*N+1,2):
    print("%d"%i,end=' ')