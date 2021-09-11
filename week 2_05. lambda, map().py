def solution(array, commands):
    answer = []
    temp = []
    for el in commands:
        i = el[0]
        j = el[1]
        k = el[2]
        
        temp =array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))

# lambda 파라미터:함수 식
# map(함수식, literal)
 
def sol(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

print(sol(array, commands))


def sol1(array, commands):
    answer = list(map(lambda x : sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    return answer

print(sol1(array, commands))
