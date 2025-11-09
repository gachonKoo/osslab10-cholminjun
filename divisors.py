import sys

number = int(sys.argv[1]) # 첫 번째 명령행 인자를 숫자로 변환

for i in range(1, number + 1): # 1부터 number까지 반복
    # number를 i로 나누었을 때 나머지가 0인지 확인 (약수인지 확인)
    if number % i == 0: 
        print(i, end=" ") # 약수를 출력 (줄바꿈 없이 공백으로 구분)

print() #
