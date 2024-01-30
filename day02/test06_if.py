# date : 20240130
# desc : 여러조건 if문

date = input('날짜를 입력하세요. ex) 12(월)-31(일) > ') # '12-31' 문자열로 입력

month = date.split('-')[0] # 입력값의 '-' 앞부분
day = date.split('-')[1] # 입력값의 '-' 뒷부분

if month == '12' and day == '25' :
    print('MERRY CHRISTMASS')
elif month == '01' and day == '01' :
    print('HAPPY NEW YEAR')
elif month == '02' and day == '14' :
    print('From Your Valentine')
else :
    print('일정이 없습니다.')