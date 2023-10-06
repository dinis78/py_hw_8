# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий

import os
import json
import csv
import pickle

def traverse_directory(directory):
    result = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)

            result.append({'name': file, 'parent_directory': root, 'type': file, 'size': size})
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                size = get_directory_size(dir_path)

                result.append({'name': dir, 'parent_directory': root, 'type': file, 'size': size})

#Сохранение
    save_as_json(result)
    save_as_csv(result)
    save_as_pickle(result)

def get_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
        return total_size
    
def save_as_json(result):
    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4)

def save_as_csv(result):
    with open('result.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'parent_directory', 'type', 'size'])
        writer.writeheader()
        writer.writerows(result)

def save_as_pickle(result):
    with open('result.pickle', 'wb') as file:
        pickle.dump(result, file)
























