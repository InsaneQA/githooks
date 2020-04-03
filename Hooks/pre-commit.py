#!/usr/bin/env python
import io
import sys
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

print(os.getcwd())
success = True
os.listdir()
print(os.listdir())
project_folder = os.getcwd()


def get_list_of_files_in_directory_and_children():
    result_files = []
    for path, folders, files in os.walk(os.getcwd()):
        result_files.extend(files)
    return result_files


def open_relative_path(relative_path: str):
    os.chdir(project_folder)
    os.chdir(relative_path)


def does_music_file_exists(path: str, filename: str) -> bool:
    is_file_exist = False
    if not is_file_exist:
        global success
        success = False
        print(u'Файл музыки не найден')


def are_graphic_elements_configured_properly() -> bool:
    pass


def are_music_files_configured_properly() -> bool:
    pass


def are_start_and_finish_dates_configured_properly() -> bool:
    pass


def main() -> int:
    does_music_file_exists('', '')
    global success
    return 0 if success else 1


if __name__ == '__main__':
    print(get_list_of_files_in_directory_and_children())
    exit(main())
