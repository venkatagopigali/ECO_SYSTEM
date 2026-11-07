'''
grades 
>=90   'A'
>=80   'B'
>=70   'C'
>=60   'D'
'''

# marks=55
# if marks>=90:           #55>=90
#     print("A grade")
# elif marks>=80:         #55>=80
#     print("B grade")
# elif marks>=70:         #55>=70
#     print("C grade")
# elif marks>=60:         # 55>=60
#     print("D grade")
# else:
#     print("No grade")


# instagram

# s_lock=1235
# a_lock=9870
# if s_lock==1234:         # 1235==1234
#     print("unlock")
#     if a_lock==9870:     # 8790==9870  
#         print("insta open")
#     else:
#         print("incorrect app password")
# else:
#     print("incorrect phone password")

'''
1 monday
2 tuesaday
3 wednessday


7 sunday

'''

# day=4
# if day==1:
#     print("monday")
# elif day==2:
#     print("Tuesday")
# elif day==3:
#     print("wednessday")
# else:
#     print("Anethor day")

day=10
match day:
    case 1:      # day==1  --> 2==1
        print("Monday")
    case 2:       # day==2  --> 2==2
        print("Tuesday")
    case 3:       # day==3  --> 3==3
        print("Wednessday")
    case _:
        print("Anethor day")
