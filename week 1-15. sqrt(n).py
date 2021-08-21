# 정수 제곱근 판별

# 문제 설명
# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 
# 제곱인지 아닌지 판단하려 합니다.
# x는 모름

# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, 
# x는 n의 제곱근 ... sqrt(n)

# n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를
# else:
#     return -1

# 완성하세요.

# 제한 사항
# n은 1이상, 50000000000000 이하인 양의 정수입니다.

import math
def solution(n):
    x = math.sqrt(n)
    if x - int(x) == 0:
        return (int(x)+1)**2
    else :
        return -1


def solution_1(n):
    for x in range(1, n):
        if n == x**2:
            return (x+1)**2
    
    else:
        return -1


def solution_2(n):
    sol = -1 if int(math.sqrt(n)) != math.sqrt(n) else (int(math.sqrt(n))+1)**2
    return sol

print(solution(36))
print(solution_1(36))
print(solution_2(36))
