'''

CSV(comma-separated values)
          필드를 쉼표(,)로 구분된
          텍스트 데이터 파일이다.
'''
student_list = []
with open('학생명단.csv', 'rt', encoding = 'UTF-8') as file:
    file.readline()
    while True:
        line = file.readline()
        if not line:
            break
            student = line.split(',')
            student_list.append(student)
print(student_list)








