s={1,2,3,4,5,6,7}
print(s)

s.add(8)
print(s)

s.update([9,10,11])
print(s)

s.remove(11)
print(s)

s.discard(12)
print(s)

#set operations
t={1,2,3,14,15,16}

#union
print(s|t)

#intersection
print(s&t)

#difference
print(s-t)
print(t-s)

#symetric difference
print(s^t)

#checking membership
print(2 in s)
print(14 in t)
print(14 in s)