import sys
import textwrap


def group(value, n):
    i = 0
    while True:
        result = value[i * n: (i + 1) * n]
        if not result:
            return
        yield result
        i += 1


def main():
    try:
        data = ''.join(sys.argv[1:])
    except IndexError:
        message = textwrap.dedent(f'''\
        Provide an argument.
        Usage: {sys.argv[0]} binary-string''')
        print(message)
        return
    try:
        chars = (chr(int(byte, 2)) for byte in group(data, 8))
        s = ''.join(chars)
    except ValueError:
        print('''Can't parse argument.''')
        return
    print(s)


if __name__ == '__main__':
    main()
