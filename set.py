s1={"a","b","c"}
s2={'d','e','d'}
#print(s1.union(s2))


#keep duplicate values while joining

s3={'a','b','c'}
s4={'b','a'}
print(s3.intersection(s4))

#keep all values except duplicate
s1.symmetric_difference_update(s2)
print(s1)
