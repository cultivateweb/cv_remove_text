from sys import argv
from cv_remove_text import cv_remove_text


def main() -> None:
    file_from = file_to = ''
    try:
        script, file_from, file_to = argv
    except ValueError:
        print(f'Error: incorrect command format. Example: {argv[0]} file_from file_to')

    print('Cleaning...')
    cv_remove_text(file_from, file_to)
    print('Complete!')


if __name__ == '__main__':
    main()
