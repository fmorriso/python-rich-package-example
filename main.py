import sys
import rich

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def main():
    pass

if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

    main()