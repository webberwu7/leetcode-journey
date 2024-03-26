def func(s: str):
    roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }
    
    answer = 0
    s_length = len(s)
    for i in range(s_length):
        if i < s_length-1 and roman[s[i]] < roman[s[i+1]]:
            answer -= roman[s[i]]
        else:
            answer += roman[s[i]]
    
    return answer

def main():
    roman_string = "XCIX"
    response = func(roman_string)

    print(response)


if __name__ == '__main__':
    main()
