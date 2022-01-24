import sys
import textwrap


def main():
    try:
        string = sys.argv[1]
    except IndexError:
        message = textwrap.dedent(f'''\
        Provide an argument.
        Usage: {sys.argv[0]} string''')
        print(message)
        return
    try:
        bytes = (format(ord(c), '08b') for c in string)
        s = ''.join(bytes)
    except ValueError:
        print('''Can't parse argument.''')
        return
    print(s)


if __name__ == '__main__':
    main()
