# 9. Write a python script to print cubes of first N natural numbers

N=int(input("Enter a number: "))

for i in range(1,N+1,1):
    print(i*i*i,end=' ')