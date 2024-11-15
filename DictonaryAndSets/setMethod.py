
# 1. add

s = {1,2,3}
s.add(563)
print(s) 

# 2. clear()
s = {1,2,3}
s.clear()
print(s)

#3. Copy
s = {1,2,3}
s1 = s.copy()
print(s1)


#4. . remove
s = {1,2,3}
s.remove(2)
print(s)

#5 .pop

s = {1,2,3}
s.pop()
print(s)

#6 union
s = {1,2,3}
s1 = {3,4,5}
print(s.union(s1))


#7 intersection
s = {1,2,3}
s1 = {3,4,5}
print(s.intersection(s1))
