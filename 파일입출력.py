# score_file = open('score.txt', 'w', encoding='utf-8')
# print('수학: 45', file=score_file)
# print('영어: 55', file=score_file)
# score_file.write('과학: 80\n')
# score_file.write('코딩: 100\n')
# score_file.close()

score_file = open('score.txt', 'r', encoding='utf-8')
print(score_file.read()) # 파일 전체의 내용을 읽어 하나의 문자열로 반환
score_file.close()
# 텍스트 파일에 쫙 써도 여기에 출력 됨

score_file = open('score.txt', 'r', encoding='utf-8')
print(score_file.read())
score_file.close()

score_file = open('score.txt', 'r', encoding='utf-8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end='')
score_file.close()

score_file = open('score.txt', 'r', encoding='utf-8')
lines = score_file.readlines() # 강사님은 이걸 선호하심
for line in lines:
    print(line, end='')
score_file.close()






