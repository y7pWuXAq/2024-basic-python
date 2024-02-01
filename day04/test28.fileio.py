# date : 20240201
# file : test28.fileio.py
# desc : 텍스트 파일 출력

# mode : a(append : 내용추가), r(read : 파일읽기), w(write : 파일읽기)
# encording : cp949(euc-kr한글), utf-8(만국 공통어)
f = open(r'sample.txt', mode='w', encoding='utf-8')  # C:\Sources\basic-python-2024\day04\sample.txt = .\day04\sample.txt
# ......... (뭔가 하기) write()에서 줄바꿈 시 문장 끝에 \n
f.write('안녕하세요, 이것은 IoT 개발자 과정입니다.\n') # mode = a, w
f.write('반갑습니다~!\n')
f.write('열심히 배워보아요!') 

f.close() # 파일은 무조건 마지막에 닫는다.
print('파일이 생성되었습니다.')