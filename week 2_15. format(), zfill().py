
# 비밀지도
# 네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 
# 비밀지도를 손에 넣었다. 
# 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 
# 확인하기 위해서는 암호를 해독해야 한다. 
# 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 
# 발견했다.

# 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 
# 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.

# 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 
# 
# 각각 "지도 1"과 "지도 2"라고 하자. 
# 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 
# 전체 지도에서도 벽이다. 
# 
# 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 
# 공백이다.
# "지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.

# 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 
# 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 
# 해당하는 값의 배열이다.


# 10진수 >> 2진수 : format(int, 'b') 
#  지정 자리수로 출력 , 공백은 0 : {:5d}.format(int)
# '{0:b}'.format(9).zfill(5)

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    answer = []
    temp = []
    
    arr1 = [list('{0:b}'.format(arr1[i]).zfill(n)) for i in range(n)]
    arr2 = [list('{0:b}'.format(arr2[i]).zfill(n)) for i in range(n)]

    for i in range(n):
        temp = []
        for e in range(n):
            if int(arr1[i][e]) ==  0 and int(arr2[i][e]) == 0:
                temp.append(' ')
            else:
                temp.append('#')
        answer.append(str(''.join(temp)))

    return answer

print(solution(n, arr1, arr2))


# ---------------------------

def sol(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        print('bin(i)다>>', bin(i)[2:])
        print('bin(j)다>>', bin(j)[2:])
        print('아 도대체 뭐야!', a12)
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

print(sol(n, arr1, arr2))