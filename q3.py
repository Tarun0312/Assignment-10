# 3. Write a python script to print first N natural numbers in reverse order

N=int(input("Enter a number: "))

for i in range(N,0,-1):
    print("%d"%i,end=' ')
