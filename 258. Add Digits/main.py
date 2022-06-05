def sumDigits(num:int)->int:
    if num == 0:
        return 0
    elif num < 10:
        return num
    else:
        return num % 10 + sumDigits(int(num/10))

def addDigits(num: int) -> int:
    while(num >= 10):
        num = sumDigits(num)
    
    return num

def main():
    num = 1444
    response = addDigits(num)

    print(response)


if __name__ == '__main__':
    main()
