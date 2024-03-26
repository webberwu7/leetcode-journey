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
    i = 0
    while(i < s_length):
        if s[i] == 'I':
            if i+1 != s_length:
                if s[i+1] == 'V' :
                    answer+= 4
                    i+=1
                elif s[i+1] == 'X':
                    answer+= 9
                    i+=1
                else:
                    answer += 1
            else:
                answer += 1
        elif s[i] == 'X':
            if i+1 != s_length:
                if s[i+1] == 'L' :
                    answer+= 40
                    i+=1
                elif s[i+1] == 'C':
                    answer+= 90
                    i+=1
                else:
                    answer += 10
            else:
                answer += 10
        elif s[i] == 'C':
            if i+1 != s_length:
                if s[i+1] == 'D' :
                    answer+= 400
                    i+=1
                elif s[i+1] == 'M':
                    answer+= 900
                    i+=1
                else:
                    answer += 100
            else:
                answer += 100
        else:
            answer += roman[s[i]]
        i+=1
        
    return answer

def main():
    roman_string = "II"
    response = func(roman_string)

    print(response)


if __name__ == '__main__':
    main()
