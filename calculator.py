def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def quo(a,b):
    return a//b

print("="*10)
print("1.덧셈\n2.뺄셈\n3.곱셈\n4.나눗셈\n5.몫 구하기\n6.끝내기")
print("="*10)

try:
    while  True:
         cal = int(input("원하는 계산기 기능의 숫자를 입력하시오: "))
         if cal <= 5:
            num1 = int(input("첫번째 숫자를 입력하세요: "))
            num2 = int(input("두번째 숫자를 입력하세요: "))
            if cal==1:
                print("결과는 {result}입니다.".format(result=sum(num1,num2)))
            elif cal==2:
                print("결과는 {result}입니다.".format(result=sub(num1,num2)))
            elif cal==3:
                print("결과는 {result}입니다.".format(result=mul(num1,num2)))
            elif cal==4:
                print("결과는 {result}입니다.".format(result=div(num1,num2)))
            elif cal==5:
                print("결과는 {result}입니다.".format(result=quo(num1,num2)))
         elif cal==6:
             print("계산기를 종료합니다.")
             break      
         else:
            print("잘못입력하셨습니다. 다시 입력해주세요.")
except ValueError:
    print("숫자를 입력해주세요. 잘못입력하여 계산기를 종료합니다.")