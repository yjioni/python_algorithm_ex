# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환
# 하는 함수, solution을 완성해 보세요. 
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환
# 하면 됩니다. 
# 
# 예를 들어 두 수 3, 12의 최대공약수는 3, 
# 최소공배수는 12이므로 solution(3, 12)는 
# [3, 12]를 반환해야 합니다.


def gcd(n, m):
    return m if n % m == 0 else gcd(m, n % m)

def lcm(n, m):
    return int(n * m / gcd(n, m))

def solution(n, m):
    return gcd(n, m), lcm(n, m)

print(gcd(3,4))

# 유클리드 호제법.....이라니!!