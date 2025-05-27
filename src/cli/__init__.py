from docopt import docopt
from . import tone
from . import file


usage = '''Usage: soundtracer tone <tone> <plugin>
       soundtracer file <file> <plugin>
       soundtracer <file> <plugin>
       soundtracer [--version | -v] [--help | -h]
'''

def main():
    args = docopt(usage)

    if args['<tone>'] is not None:
        tone.matcher(args['<tone>'], args['<plugin>'])
    elif args['<plugin>'] is not None:
        file.matcher(args['<file>'], args['<plugin>'])
    else:
        print(usage)
        


if __name__ == "__main__":
    main()