# date : 20240130
# file : test12_dictionary.py
# desc : 복합 자료형 딕셔너리

## 사전형 : key와 value쌍을 나열해 놓은 자료형
# { key : vlaue, key : vlaue, key : vlaue, key : vlaue ... }

dict_movie = {'name' : '어벤저스 엔드게임', 'type' : '히어로 무비' , 'year' : 2019, 
              'dorector' : ['안소니 루소', '조 루소'],
              'cast' : ['아이언맨', '타노스', '헐크', '토르', '닥터스트레인지']}

print(dict_movie['name'])
print(dict_movie['year'])

# 추가, 수정
dict_movie['year'] = 2020
print(dict_movie)

dict_movie['producer'] = '케빈 파이기'
print(dict_movie)

# 딕셔너리에 key 값이 있는지 확인 할 때
if 'musician' in dict_movie : 
    print(dict_movie['musician'])
else :
    print('음악감독 정보 확인 불가')

musician = dict_movie.get('musician')
print(musician)
#print(dict_movie['musicain']) > 오류(예외) 발생

## 반복문으로 출력
print(' --- 반복문 출력 ---')
for key in dict_movie :
    print(key, ':', dict_movie[key])

print('-- 다른 방식으로 출력 --')
for key, value in dict_movie.items() :
    print(key, ':', value)