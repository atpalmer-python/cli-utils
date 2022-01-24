import io
import sys
import click
from . import serde


CHOICE = click.Choice(serde.CHOICES)


@click.option('-o', '--out', 'out_format', default='json', type=CHOICE, help='Format of data read from STDIN')
@click.option('-i', '--in', 'in_format', default='json', type=CHOICE, help='Format of data written to STDOUT')
@click.command()
def main(in_format, out_format):
    load, dump = serde.get(in_format, out_format)
    try:
        dump(load(sys.stdin), sys.stdout)
    except Exception as e:
        sys.stderr.write('Parse Error: {}\n'.format(str(e)))
