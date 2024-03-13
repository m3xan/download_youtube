"""
Для генерации файлов
"""

import os
import re
from typing import Generator

def ui_file_directory(path: str) -> Generator[str, None, None]:
    """
    Возвращает все файлы в директории с .ui
    """
    files = os.listdir(path)
    pattern = re.compile(r'.*\.ui')
    for it in files:
        if pattern.match(it):
            yield it

def generate_class_ui_to_py(path: str):
    """
    Генерирует из ui в py все файлы в директории
    """
    for file in ui_file_directory(path):
        file_path = os.path.join(path, file)
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyside6-uic {file_path} -o {path}{os.sep}{file_name_without_extension}_class.py'
        os.popen(cmd)
        print('Успешная генерация файла')

if __name__ == '__main__':
    window_paths = [
       f'{os.getcwd()}\\window'
    ]
    for path in window_paths:
        generate_class_ui_to_py(path)
