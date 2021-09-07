# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
# 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 
# solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.
# 입출력 예
# prices           	return
# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

def solution(prices):
    answer = []
    
    while prices:
        
        a = prices.pop(0)
        count = 0
        
        for price in prices: 
            count += 1
            if a > price: break
        answer.append(count)

    return answer

print(solution([1, 2, 3, 2, 3]))


def solution1(prices):
    # answer = 몇초 후 가격이 떨어지는지 저장하는 배열
    answer = [len(prices)-i-1 for i in range(len(prices))]
    
    # stack = prices의 인덱스를 차례로 담아두는 배열
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]
            print('index는, ', index)
            # 주식 가격이 떨어졌다면
            if prices[index] > prices[i]:
                print('prices[index], prices[i] 순서', prices[index], prices[i])
                answer[index] = i - index
                stack.pop()
            
            # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다는 말)
            else:
                break
        
        # 스택에 추가한다.
        # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정이다.
        stack.append(i)
        
    return answer

print(solution1([1, 2, 3, 2, 3]))
