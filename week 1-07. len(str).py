# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 입출력 예
# s	        return
# "abcde"	"c"
# "qwer"    "we"

def solution(s):
    
    length = len(s)
    
    if length % 2 == 0: 
        answer = s[length//2-1 : length//2+1] # 4 >> s[1:3] --> 2개
    else:
        answer = s[length//2] # s[2]
    return answer

print(solution('gucci'))


# 다른 방식
def string_middle(str):

    return str[(len(str)-1)//2:len(str)//2+1] # 4 >> s[1: 3]
                                              # 5 >> s[2: 3]

print(string_middle("power"))