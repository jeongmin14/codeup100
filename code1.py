# 6006
# 다음 문장을 출력하시오.
# "!@#$%^&*()'
# (단, 큰따옴표와 작은따옴표도 함께 출력한다.)
# 출력 형식에 필요한 따옴표와 출력할 문자인 따옴표를 구분하기 위하여
# \" 또는 \' 를 이용하여 출력할 수 있다.
# print("\"!@#$%^&*()\'")

# 6007
# 다음 경로를 출력하시오.
# "C:\Download\'hello'.py"
# (단, 따옴표도 함께 출력한다.)
# print("\"C:\\Download\\'hello'.py\"")

# 6009
# 변수에 문자 1개를 저장한 후
# 변수에 저장되어 있는 문자를 그대로 출력해보자.
# c = input()
# c = "a"
# print(c)

# 6010
# 변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.
# n = input()
# n = int(15)
# print(n)

# split, sep, join 연습
# m = "2021-03-22"
# s = m.split("-") #변수로 저장한 날짜를 "-"기준으로 쪼개어 리스트로 저장
# print(s,sep=":")
# print(s) #출력결과 ['2021', '03', '22']
# print(":".join(s)) #출력결과 2021:03:22
# join을 이용하여 배열을 합차고 따옴표안에 있는 기호로 요소들을 분리?구분?
# print(",".join(s)) #출력결과 2021,03,22

# a="apple"
# b="banana"
# print(a,b) #default는 공백으로 구분
# print(a,b,sep='-') #출력결과 apple-banana
# 공백이 아닌 다른 문자를 넣어주고 싶을 때 sep='[문자]' ex)sep=':'

# 6019
# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.
# y,m,d = "2021.3.22".split('.') #'.'기준으로 쪼개어 저장 
# print(y,m,d) #출력결과 2021 3 22
# print(d,m,y,sep='-') #출력결과 22-3-2021

# 6020
# 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
# 주민번호를 입력받아 형태를 바꿔 출력해보자.
# birth, code = "940214-2000000".split('-')
# '-'기준으로 앞자리는 birth라는 변수에 저장, 뒷자리는 code라는 변수에 저장
# print(birth, code, sep='') #공백없이 붙여서 출력

# umber = "940214-2000000".split('-')
# 앞자리, 뒷자리 구분 하지 않고 하나의 변수에 저장할 경우 ['940214', '2000000']인 리스트에 담겨서 출력된다.
# print(''.join(number)) #출력결과 9402142000000 .join()안에는 하나의 argument만 올 수 있음

# 6023 
# 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.
# h, m, s = "17:23:57".split(':')
# print(m)

# 6024
# 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아 순서대로 붙여 출력하는 프로그램을 작성해보자.
# w1, w2 = input().split()
# s=w1+w2
# print(s)

# 6025
# 정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
# a, b ='7,8'.split(',')
# c = int(a)+int(b)
# print(c)

# 6026
# 실수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
# a, b ='3.1,4.4'.split(',')
# c= float(a)+float(b)
# print(c)

# 6027
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.
# a=255
# n=int(a)
# print('%x'%n) #16진수로 출력

# 6030
# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
# n=ord('A') #괄호안의 문자를 10진수 유니코드값으로 변환 후 n이라는 변수에 저장
# print(n) #출력결과 65

# 6031
# 10진 정수 1개를 입력받아 유니코드 문자로 출력해보자.
# c = int(65)
# print(chr(c))

# 6032
# 입력된 정수의 부호를 바꿔 출력해보자.
# n =int(8) #int를 이용하여 정수로 변환하여 n이라는 변수에 저장
# print(-n) #저장된 변수n은 정수이기때문에 앞에 -붙여줌으로써 부호가 바뀐다.

# 6033
# 문자 1개를 입력받아 그 다음 문자를 출력해보자. 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.
# n = ord('b') #문자 a를 10진수로 변경하여 n이라는 변수에 저장
# print(chr(n+1)) #변수n에 저장된 10진수의 값에 1을 더하여 그 값을 유니코드 문자로 변환

# 6036
# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.
# w, n = input().split()
# w, n = 'love 3'.split()
# print(w*int(n))

# 6037
# 반복 횟수와 문장을 입력받아 여러 번 출력해보자.
# n = 3
# s = 'hello world'
# print(int(n)*s)

# 6044
# 정수 2개(a, b)를 입력받아 자동 계산하기
# 합, 차, 곱, 몫, 나머지, 나눈 값 순서로
# a, b ='10,3'.split(',')
# int_sum = int(a)+int(b)
# int_sub = int(a)-int(b)
# int_mul = int(a)*int(b)
# int_div = int(a)//int(b)
# int_q = int(a)%int(b)
# int_u = int(a)/int(b)
# print(int_sum)
# print(int_sub)
# print(int_mul)
# print(int_div)
# print(int_q)
# print(int_u)
# print('%.2f'%int_u) #소수점 셋재 자리에서 반올림하여 둘째자리까지 출력할 경우

# 6045
# 정수 3개를 입력받아 합과 평균을 출력해보자
# a,b,c = '1 2 3'.split()
# d=int(a)+int(b)+int(c)
# e=d/3
# print(d, '%.2f'%e)

# 6046
# 정수 1개를 입력받아 2배 곱해 출력해보자.
# n=1024
# print(n<<1) #1024를 2배한 값인 2048이 출력된다.
# print(n>>1) #1024를 반으로 나눈 값
# print(n<<2) #1024의 2배의 2배, 1024*2^2
# print(n<<3) #1024의 2배의 2배의 2배, 1024*2^3

# 6047
# 정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.
# a,b = '1 3'.split()
# print(int(a)<<int(b)) #int(a)*2^int(b)

# 6048
# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.
# a, b ='1 9'.split()
# print(int(a)<int(b))

# 6049
# a와 b의 값이 같은 경우 True 를, 그렇지 않은 경우 False 를 출력한다.
# a, b ='0 0'.split()
# print(int(a)==int(b))

# 6050
# a, b ='0 -1'.split()
# print(int(a)<=int(b))

# 6052
# 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.
# n = int(1) #0일때 False, 1일때 True
# print(bool(n))

# 6053
# 정수값이 입력될 때, 그 불 값을 반대로 출력하는 프로그램을 작성해보자.
# a = bool(int(1))
# print(a) #출력결과 True
# print(not a) #not이라는 예약어를 통해 참, 거짓 논리값을 바꿀 수 있다. 출력결과 False

# 6054
# 2개의 정수값이 입력될 때, 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.
# a, b = '1 0'.split()
# print(bool(int(a)) and bool(int(b))) 
# and예약어는 두 불값이 모두 참일 때 True, 하나라도 거짓일 경우 False가 출력된다.

# 6056
a = bool(int(1))
b = bool(int(1))
print((a and (not a)) or (b and (not b))) 