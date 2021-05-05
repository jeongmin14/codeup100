# 10진수에서 2진수, 8진수, 16진수 변환
# a=123

# b=bin(a) #2진수 변환함수, 숫자앞에 0b가 붙는다.
# o=oct(a) #8진수 변환함수, 숫자앞에 0o이 붙는다.
# h=hex(a) #16진수 변환함수, 숫자앞에 0x가 붙는다.

# print(b)
# print(o)
# print(h)

# 6063
# 정수 2개 입력받아 큰 값 출력하기
# a,b=input("숫자2개입력: ").split()
# a=int(a)
# b=int(b)
# c = (a if a>b else b)
# print(int(c))

# 6064
# 정수 3개를 받아서 가장 작은 값을 출력하기
# a,b,c=input("숫자 3개 입력: ").split()
# a=int(a)
# b=int(b)
# c=int(c)
# d = (a if a<b else b) if ((a if a<b else b)<c) else c
# print(int(d))

# 6065
# 정수 3개 입력받아 짝수만 출력하기

# a,b,c = input("숫자 3개입력 : ").split()
# a=int(a)
# b=int(b)
# c=int(c)
# if a%2==0:
#     print(a)
# if b%2==0:
#     print(b)
# if c%2==0:
#     print(c)
    
# def even(num):
#     if num%2==0:
#         return num
# print(even(a))
# print(even(b))
# print(even(c))
# 20210505
