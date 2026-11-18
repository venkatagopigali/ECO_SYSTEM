# a=[]
# print(type(a))

# a=list()
# print(type(a))

# l=[10,20,40,50,60,'python','eco']
# l[1]=70
# print(l)


# l=[10,30,10,40,50,20,10,20,40,30,20]
# print(l)


# a=[10,20,30,'python',5.6,True,None]
# print(type(a[3]))

# a=[10,20,30,'python',5.6,True,None]
# for i in a:
#     print(i)


# a=[10,20,30,'python',5.6,True,None]
# i=0
# while i<len(a):
#     print(a[i])
#     i=i+1

#    0   1  2    3       4     5     6
# a=[10,20,40,'python','gopi',40.5,80.9]
#    -7 -6 -5    -4      -3    -2    -1
# print(a[3])
# print(a[-4])
# print(a[1:6:2])
# print(a[-6:-1:2])

# a=[10,40,20,50,'python']
# a.append([100,20,30,40])
# print(a)

# a=[10,40,20,50,'python']
# a.extend([100,20,30,40])
# print(a)



# a=[10,40,20,50,'python']
# a.extend([100,30,40,80])
# print(a)

# a=[10,20,40,50]
# a.extend("python")
# print(a)


# a=[10,20,'gopi','python',90]
# a.insert(2,100)
# print(a)


# a=[10,20,'gopi','python',90]
# a.pop()
# print(a)


# a=[10,20,'gopi','python',90]
# a.pop(2)
# print(a)

# a=[10,20,'gopi','python',90]
# a.remove('gopi')
# print(a)


# a=[10,20,'gopi','python',90,'gopi']
# print(a.index('gopi',3))
# print(len(a))
# print(a.count('python'))

# import copy
# a=[10,20,'gopi','python',90,'gopi']
# b=copy.copy(a)
# b=a.copy()
# b[1]=[123]
# print(b)

# print(a)

# import copy
# a=[10,20,30,40,50]
# b=copy.copy(a)
# b[2][0]=100
# print(b)
# print(a)

# a=[10,20,40,50,20,40,99,8,6,2]
# a.clear()
# print(a)


# a=[10,20,40,50,20,40,99,8,6,2]
# a.sort(reverse=True)
# print(a)

# a=[10,20,40,50,20,40,99,8,6,2]
# a.reverse()
# print(a)