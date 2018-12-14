# def add(a,b):
#     r=a+b
#     return r
# # call func
# s = add(3,6)
# print(s)

# 1 ham ten la eval
from random import randint, choice

op_list = ["+", "-", "*", "/"]
op = choice(op_list)
a = randint(0, 10)
b = randint(0, 10)
err = choice([-2, -1, 0, 0, 1, 2, 0])

def eva(a,b,op):
    if op == '+':
        r = a+b
    elif op == '-':
        r = a-b
    elif op == '*':
        r = a*b
    elif op == '/':
        # if a == 0 or b == 0:
        #     print("vo nghiem")
        # else:
        r = a/b
    else:
        print("Unsupported operator")
    return r

# s = eva(a,b,op)
# print(a,op,b,"=",s)
