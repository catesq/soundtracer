from docopt import docopt
import pprint
import commands 


usage = '''Usage: soundtrace tone <tone> <plugin> [--qfactor <q> | -Q <q>] [--harmonic <h> | -H <h>] [--input <input> | -I <input> ] [ --sr | -S <samplerate> ]
    soundtrace file <file> <plugin>
    soundtrace <file> <plugin>
    soundtrace list [<type>]
    soundtrace [--version | -v] [--help | -h]

Options:
    --qfactor <q>, -Q <q>         # Q factor for the tone (optional) [default: 1.0]
    --harmonic <h>, -H <h>        # harmonic strength factor (optional) [default: 0.5]
    --input <input>, -I <input>   # Input for processing (optional)
                                  #     audio file if first plugin is an effect 
                                  #     midi note/midi file if first plugin is an instrument
    <tone>                        # The tone to match, can be a note or frequency (e.g. A4 or 440 or 0.44k)
    <file>                        # The audio file to process
    <plugin>                      # The plugin to use for matching
    --version -v                  # Show version information
    --help -h                     # Show this help message
'''


def main():
    """
    Main entry point for the soundtrace CLI.
    Parses command line arguments and dispatches one of the modules in src/commands 
    """
    args = docopt(usage)

    if args['<tone>'] is not None:
        commands.tone.matcher(args['<tone>'], args['<plugin>'], args['--input'], args['--qfactor'], args['--harmonic'])
    elif args['<file>'] is not None:
        commands.file.matcher(args['<file>'], args['<plugin>'])
    elif args['list']:
        pprint.pp(commands.list_plugins(args['<type>']))
    else:
        print(usage)


if __name__ == "__main__":
    main()