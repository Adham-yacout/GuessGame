
from random import randint
total_scr = 0
tries = 10
level = 1

while level <=10:
    punish= 100/tries
    tn=randint (1, 10)
    cnt=0
    print("you are in level: ", level)

    opt=int (input("1-help 2-not:"))
    while cnt < tries:# cnt#9 <9
        gn=int (input("enter your guess:")) #gn=
        if gn == tn:
                print ("True guess")
                level+=1
                tries-=1
                break
        cnt=cnt+1
        if cnt < 10:
          if opt ==1:

            if gn < tn:
                  print("wrong guess.. go high")

            elif gn > tn:

                    print("wrong guess.. go low")

            else:
                print ("wrong guess....try again")

    else:

        print("you lost this level...pleas try again")
        score=100-punish*cnt

        print ("your scores=", round (score))
        total_scr=total_scr+score

        print ("total score=",round(total_scr))
