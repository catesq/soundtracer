import argparse



def build_parser():
    parser = argparse.ArgumentParser(description="matcher")
    subparser = parser.add_subparsers()
    tone_p =  subparser.add_parser("tone", help="Tone matcher")
    tone_p.add_argument("tone", type=str, help="Tone in hz or note name eg (A4, C#5, Fb, C+)")

    return parser


def main():
    p = build_parser()
    (args, extra) = p.parse_known_args()


    plugin = False
    if len(extra) > 0:
        plugin = extra[0]

    print("plugin: {plugin}")

    if hasattr(args, 'tone'):
        print(f"Tone: {args.tone}")
    else:
        p.print_help()

if __name__ == "__main__":
    main()