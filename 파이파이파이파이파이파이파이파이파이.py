def season():
    while True:
        a = int(input())
        if a >= 3 and a <= 5:
            print("spring")
        if a >= 6 and a <= 8:
            print("summer")
        if a >= 9 and a <= 11:
            print("fall")
        if a == 12 or a == 1 or a == 2:
            print("winter")
season()