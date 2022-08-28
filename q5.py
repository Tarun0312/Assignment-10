# 5. Write a python script to print first N odd natural numbers in reverse order


N=int(input("Enter a number: "))

for i in range(2*N-1,0,-2):
    print("%d"%i,end=' ')