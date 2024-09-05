marks1=int(input("enter the marks1"))
marks2=int(input("enter the marks2"))
marks3=int(input("enter the marks3"))

#for total percentage

total_percentage= (100*(marks1+marks2+marks3)/300)

if (total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed")
else:
    print("you are failed")