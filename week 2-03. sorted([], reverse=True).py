# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.


print('----문제오인-----')
print('숫자열 정렬')
def solution(n):
    n =  map(int, sorted(str(n), reverse=True))
    answer = list(n)
    return answer


print('-'*50)
n = 12346
answer=[]

def so(n):
    n = list(str(n))
    while n:
        answer.append(int(n.pop()))
    return answer

print(so(12345))

print('-'*50)

def so1(n):
    answer = list(map(int, list(str(n)[::-1])))
    return answer

print(so1(12344))

def so2(n):
    answer = list(map(int, reversed(str(n))))
    return answer
print(so2(12949))