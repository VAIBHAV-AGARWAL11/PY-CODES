'''
star pattern for n=3
  *
 ***
*****  


'''

n=int(input("enter the number"))
for i in range(1,n+1):
    print(" "*(n-i),end="")#this is for printing space
    print("*"*(2*i-1),end="")#this is for printing the star
    print("\n")#new line character
