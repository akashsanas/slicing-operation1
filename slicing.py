s = "Akashsanas" #string

print(len(s)) #total length of string


#5 positive + positive index
print(s[0:10]) #whole positive index
print(s[5:11])#pritn last 5 varables
print(s[0:5])#print first 5 varables
print(s[1:5])#print middle world
print(s[2:7])#print middle world

# 5 negative + negative index

print(s[ -12:-5:])#negative index
print(s[-5: ]) #skping last element
print(s[-7:-3])#negative index
print(s[-10:-5])#negative index
print(s[-10:])#skping single element

# 5 positive + negative index

print(s[0: ])#skping single element
print(s[5:-1])
print(s[0:-5])
print(s[ : -1])
print(s[7:-1])

# 5 negative + positive index

print(s[-10:5])
print(s[-5:10])
print(s[-9:5])
print(s[-4:10])
print(s[-7:9])

# 5 on positive step size

print(s[0:11:1])
print(s[0:10:2])
print(s[0:10:3])
print(s[0 : 10:4])
print(s[0:10:5])

# 5 on negative step size

print(s[10: : -1])
print(s[10: 0:-2])
print(s[10:5:-2])
print(s[10:-9:-1])
print(s[10:0:-4])