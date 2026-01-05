import sys


def get_file_contents() -> str:
    path = "data/"+get_path()
    try:
        with open(path, mode='r') as file:
            return file.read()
    except OSError as e:
        print('Failed to open file', e)
    except Exception as e:
        print('Error', e)


def main():
    file_contents = get_file_contents()
    print(file_contents)


def get_path() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return ''



if __name__ == "__main__":
    main()
