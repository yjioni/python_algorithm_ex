# 문제 설명
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수,
# solution을 완성하세요.
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# 제한 조건
# n은 길이 10,000이하인 자연수입니다.

get_string = input("A word ? >>")
get_num = int(input("numbers >>"))

def solution(n):
    answer = ''
    str = get_string * n
    
    return str[:n]

print(len(solution(get_num)))
print(solution(get_num))


