year = int(input(("연도를 입력하시오.")))
if((year % 4 == 0) and (year % 100 != 0)):
    print("윤년입니다.")
else:
    if(year % 400 == 0):
        print("윤년입니다.")
    else:
        print("윤년이 아닙니다.")