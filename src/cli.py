from docopt import docopt

from commands import tone, file


usage = '''Usage: soundtracer tone <tone> <plugin>  
       soundtracer file <file> <plugin>
       soundtracer <file> <plugin>
       soundtracer [--version | -v] [--help | -h]
'''


def main():
    """
    Main entry point for the soundtracer CLI.
    Parses command line arguments and dispatches to a sound matcher.
    """
    args = docopt(usage)
    
    if args['<tone>'] is not None:
        tone.matcher(args['<tone>'], args['<plugin>'])
    elif args['<file>'] is not None:
        file.matcher(args['<file>'], args['<plugin>'])
    else:
        print(usage)

        
if __name__ == "__main__":
    main()