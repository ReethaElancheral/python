from calc.interface import get_parser, execute

def main():
    parser = get_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
    else:
        execute(args)

if __name__ == "__main__":
    main()
