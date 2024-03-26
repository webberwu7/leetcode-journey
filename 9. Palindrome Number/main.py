def isPalindrome(x: int) -> bool:
    string_x = str(x)
    string_x_length = len(string_x)
    for i in range(int(string_x_length/2)):
        if string_x[i] != string_x[-1-i]:
            return False

    return True

def main():
    num = 12
    response = isPalindrome(num)

    print(response)


if __name__ == '__main__':
    main()
