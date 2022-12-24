import random
n1 = int(random.randint(1,101))
while True:
    p1 = int(input())
    if n1 < p1:
        print("Down")
    if n1 > p1:
        print("Up")
    if n1 == p1:
        print("Correct")
        break