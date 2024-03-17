"""
Для генерации файлов
"""

import os
import re
import subprocess
import concurrent
from concurrent.futures import ProcessPoolExecutor


PATHS = [
    'window'
]

def find_ui_file(path: str):
    """Находит .ui файл в директории"""
    files = os.listdir(path)
    pattern = re.compile(r'.*\.ui')
    for file in files:
        if pattern.match(file):
            return file
    return None

def generate_class_ui2py(path: str):
    """
    Заглушка
    """
    ui_file = find_ui_file(path)
    if ui_file is None:
        print('В директории файла нет')
    else:
        file_path: str = os.path.join(path, find_ui_file(path))
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyside6-uic {file_path} -o {path}{os.sep}{file_name_without_extension}_class.py'
        try:
            subprocess.run(
                cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8'
            )
            print('Успешная генерация файла')
            return f'{path}{os.sep}{file_name_without_extension}_class.py'
        except subprocess.CalledProcessError as e:
            print('Ошибка при генерации файла')
            raise e
    return None

def generate_window_wisout_changes(paths: list):
    """делает файлики окон из директорий"""
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(generate_class_ui2py, path): path for path in paths}
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                raise e

if __name__ == '__main__':
    generate_window_wisout_changes(PATHS)
