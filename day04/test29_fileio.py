# date : 20240201
# file : test29_fileio.py
# desc : 텍스트 파일 읽기

f = open('sample.txt', mode='r', encoding='utf-8')
# 읽기 완료!
# text = f.read() # 텍스트 파일의 모든 텍스트를 전부 한번에 읽어오는 것. 단, 파일 용량이 크면 X
# print(text)

# 가장 일반적인 형태
while True :
    line = f.readline()
    if not line : break # 조건문, 반복문 내의 코드가 한줄인 경우 if 옆에 바로 적을 수 있음.
    print(line.replace('\n', ''))

f.close()