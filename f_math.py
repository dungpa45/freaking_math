from random import randint,choice
from func_intro import eva
import mlab
from highscore import Highscore

mlab.connect()

def generate_quiz():

    x = randint(-100,100)
    y = randint(-100,100)
    # err = randint(-2,2)
    # err = choice([10,0])
    # err = choice([0,0.1])
    err= choice([0,10])
    o = choice(["*"])
    r = eva(x, y, o) + err

    return x,y,o,r,err

# diem =0
# name = input("Your name: ")
# while True:
#     a, b, op, r,err = generate_quiz()


#     print(a,op,b,"=",r)
#     chon = input("Y / N  :")
#     if chon =="y":
#         if err == 0:
#             print("Bingo")
#             diem +=1
#         else:
#             print("fail")
#             print(name,diem)
#             highscore = Highscore(name=name, diem=diem)
#             highscore.save()
#             break
#     else:
#         if err==0:
#             print("Fail")
#             print(name,diem)
#             highscore = Highscore(name=name,diem=diem)
#             highscore.save()
#             break
#         else:
#             print("Bingo")
#             diem +=1


record = Highscore.objects()
li =[]
for r in record:
    print(r.name,r.diem)
    li.append(r.diem)
print(sorted(li, reverse=True))
