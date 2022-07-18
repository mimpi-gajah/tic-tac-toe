<문제 1>
from random import randint

maxHit =randint(7, 12) # 내구력: 7~12
per = randint(1, 10)

while maxHit > 0:
    input("나무 내구력:"+str(maxHit) + " -> HIT!! ")
    
    if per == 1: # 10% 확률
        print("크리티컬!!")
        maxHit -= 3
    elif per == 2: # 10% 확률로 도끼놓침
        print("나무 베기가 불가능합니다")
        break
    else: # 90% 확률
        maxHit -= 1

else: print("나무가 넘어갔습니다.")