# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.

def solution(n):
    answer = []
    for i in range(1, n+1):
        if n%i == 0:
            answer.append(i)
    return "{}의 약수는 {}입니다. 이를 모두 더하면 {}입니다."\
            .format(n, ", ".join(map(str, answer)), sum(answer))

# test
print(solution(12))
    