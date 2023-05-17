f = open('C:/Users/farid/Desktop/example.txt', 'r')
line=f.readline() #Читает по строкам
print(line, end='') #Выводит без символа перевода строки


with open('C:/Users/farid/Desktop/example.txt', 'w') as f: #Запись данных
    f.write("Ваши данные здесь")

print(f"Данные сохранены в файле: {'C:/Users/farid/Desktop/example.txt'}")
f.close() #закрывает файл