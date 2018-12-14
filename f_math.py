from random import randint,choice
from func_intro import eva
import mlab
from highscore import Highscore

mlab.connect()

def generate_quiz_easy():
    x = randint(0, 25)
    y = randint(0, 25)
    err = randint(-2, 2)
    o = choice(["+", "-", "*", "/"])
    r = eva(x, y, o) + err

    return x, y, o, r, err


def generate_quiz_normal():
    x = randint(-25, 25)
    y = randint(-25, 25)
    o = choice(["+", "-", "*", "/"])
    if o == "*":
        err = choice([0,10])
    elif o == "/":
        err = choice([0,0.1])
    else:
        err = randint(-2, 2)

    r = eva(x, y, o) + err

    return x, y, o, r, err


def generate_quiz_hard():

    x = randint(-100,100)
    y = randint(-100,100)
    # err = choice([10,0])
    # err = choice([0,0.1])
    o = choice(["+","-","*","/"])
    if o =="/":
        err = choice([0,0.1])
    else:
        err = choice([0, 10])

    r = eva(x, y, o) + err

    return x,y,o,r,err 

diem =0
name = input("Your name: ")
level = input("easy, normal, hard:  ")
if level=="easy":
    while True:
        a, b, op, r,err = generate_quiz_easy()

        print(a,op,b,"=",r)
        chon = input("Y / N  :")
        if chon =="y":
            if err == 0:
                print("Bingo")
                diem +=1
            else:
                print("fail")
                print(name,diem)
                highscore = Highscore(name=name, diem=diem,level=level)
                highscore.save()
                break
        else:
            if err==0:
                print("Fail")
                print(name,diem)
                highscore = Highscore(name=name,diem=diem,level=level)
                highscore.save()
                break
            else:
                print("Bingo")
                diem +=1

elif level=="normal":
    while True:
        a, b, op, r, err = generate_quiz_normal()

        print(a, op, b, "=", r)
        chon = input("Y / N  :")
        if chon == "y":
            if err == 0:
                print("Bingo")
                diem += 1
            else:
                print("fail")
                print(name, diem)
                highscore = Highscore(name=name, diem=diem,level=level)
                highscore.save()
                break
        else:
            if err == 0:
                print("Fail")
                print(name, diem)
                highscore = Highscore(name=name, diem=diem,level=level)
                highscore.save()
                break
            else:
                print("Bingo")
                diem += 1

elif level=="hard":
    while True:
        a, b, op, r, err = generate_quiz_hard()

        print(a, op, b, "=", r)
        chon = input("Y / N  :")
        if chon == "y":
            if err == 0:
                print("Bingo")
                diem += 1
            else:
                print("fail")
                print(name, diem)
                highscore = Highscore(name=name, diem=diem,level=level)
                highscore.save()
                break
        else:
            if err == 0:
                print("Fail")
                print(name, diem)
                highscore = Highscore(name=name, diem=diem,level=level)
                highscore.save()
                break
            else:
                print("Bingo")
                diem += 1

print("==================HIGHSCORE==================")
record = Highscore.objects(level__exact=level)
print("Level",level)
li =[]
for r in record:
    li.append((r.diem, r.name))
    li.sort(reverse=True)
rank=0
for i,j in li:
    rank+=1
    print(rank,j,i,sep=': ')
