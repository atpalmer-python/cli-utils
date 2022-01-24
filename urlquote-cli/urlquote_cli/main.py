from urllib.parse import quote
import sys


def main():
    for text in sys.argv[1:]:
        print(quote(text))
