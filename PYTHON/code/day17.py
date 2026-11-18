# a='python programing'
# print(a.split(" "))

# print("eco"+" "+"system"+" "+"python")


# a=["eco","system","python"]
# # print(" ".join(a))
# b=""
# for i in a:
#     b=b+i+" "
# print(b)


# a="ecosystem"
# print(a.startswith('eco'))
# print(a.endswith('m'))

# print(ord('A'))
# print(ord('a'))
# print(ord(" "))

# print(chr(67))
# print(chr(100))

# a="eco system"
# print(a.__contains__('S'))
# print(a.count('M'))


# a="eco4$*"
# print(a.isupper())
# print(a.islower())


# a="Eco System 0Python"
# print(a.istitle())
# a="Eco"
# print(a.isalpha())

# a="23456"
# print(a.isdigit())

# a="123qbd."
# print(a.isalnum())

# a=" "
# print(a.isspace())

## a-z

# print(ord('a'))
# print(ord('z'))

# for i in range(ord('a'),ord('z')+1):
#     print(chr(i))

# print(ord('a'))
# print(ord('A'))


# a="EcoSystem"
# b=""                          # b=ECO
# for i in a:                  # o
#     if i.isupper():          # false 
#         b=b+i
#     else:
#         b=b+chr(ord(i)-32)    
# print(b)

# print(ord('E'))

# a="Ecosystem"
# b=""
# for i in a:      
#     if ord(i)>=ord('a') and ord(i)<=ord('z'):
#         b=b+chr(ord(i)-32)
#     else:
#         b=b+i
# print(b)


# a="ecosystem ."
# c=0
# for i in a:
#     c=c+1
# print(c)

# a="ecosystem"
# c=0
# for i in a:
#     if i=="M":
#         c=c+1
# print(c)

# a="ecosystem"
# print(len(a)-len(a.replace('s','')))

# a="ecosyatem"
# b=""
# old="a"
# new="s"
# for i in a:
#     if i==old:
#         b=b+new
#     else:
#         b=b+i
# print(b)


# a="     eco system       "
# b=""
# ls=""
# rs=""
# # for i in a:
# #     if i!=" ":
# #         b=b+i
# # print(b)
# for i in a:
#     if i==" ":
#         ls=ls+i
#     else:
#         break
# for i in range(-1,-len(a),-1):
#     if a[i]==" ":
#         rs=rs+a[i]
#     else:
#         break
# b=a.replace(ls,"")
# c=b.replace(rs,"")
# print(c)


a=[[10,20,30],
   [40,50,60],
   [70,80,90]]
sum=0               # 60
for i in a:       # [40,50,60]
    for j in i:      # 40
        sum=sum+j
print(sum)