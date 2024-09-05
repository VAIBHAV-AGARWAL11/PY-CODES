#three arrays, to find the common elements of the three arryas
#ar1=[1,5,10,20,40,80]
#ar2=[6,7,20,80,100]
#ar3=[3,4,15,20,30,70,80,120]
#output=[80,20]

ar1=[1,5,10,20,40,80]
ar2=[6,7,20,80,100]
ar3=[3,4,15,20,30,70,80,120]

#type cast into sets
s1=set(ar1)
s2=set(ar2)
s3=set(ar3)

#join using intrsection
s1s2=s1.intersection(s2)
final_set=s1s2.intersection(s3)
lst=list(final_set)
print(lst)


