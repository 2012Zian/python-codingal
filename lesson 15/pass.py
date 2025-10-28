for num in range(20):
    if num % 20 == 0:
        print("num is divisible by 20")
    elif num % 15 == 0:
        pass
    elif num % 5 == 0:
        print("num is divisible by 5")
    elif num % 3 == 0:
        print("num is divisible by 3")
    else:
        print(num)