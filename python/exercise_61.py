import os

# Укажите абсолютный путь к новой папке
folder_path = "C:/Users/farid/Desktop/new_folder"

# Создаем новую папку, если она еще не существует
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Создаем файл с данными в новой папке
file_path = os.path.join(folder_path, "example.txt")

with open(file_path, "w") as f:
    f.write("Ваши данные здесь")

print(f"Данные сохранены в файле: {file_path}")
