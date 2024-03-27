def func(strs):
    sorted_strs = sorted(strs, key=len)
    
    answer = ""
    for i in range(len(sorted_strs[0])):
        for str in sorted_strs[1:]:
            if sorted_strs[0][i] != str[i]:
                return answer
        
        answer += sorted_strs[0][i]
    
    return answer
         
def main():
    strs = ["flower","flow","flight"]
    response = func(strs)

    print(response)


if __name__ == '__main__':
    main()
