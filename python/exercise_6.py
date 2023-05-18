#f = open(file_name, access_mode)
f = open('C:/Users/farid/Desktop/example.txt', 'r')
line=f.readline() #Читает по строкам
print(line, end='') #Выводит без символа перевода строки
f.close() #закрывает файл
