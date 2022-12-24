print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n값을 입력하세요.: '))
num = 0
i = 1
while i <= n:
  num = num + i
  i = i + 1
print(f'1부터 {n}까지 정수의 합은 {num}입니다.')