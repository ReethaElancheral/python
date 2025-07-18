import argparse
import calc.basic as b
import calc.advanced as adv

def get_parser():
    parser = argparse.ArgumentParser(description="Command Line Calculator")

    subparsers = parser.add_subparsers(dest='command', help='Operation to perform')

    # Basic operations
    for op in ['add', 'subtract', 'multiply', 'divide', 'power']:
        p = subparsers.add_parser(op)
        p.add_argument('a')
        p.add_argument('b')

    # Advanced (single input)
    sqrt_parser = subparsers.add_parser('sqrt')
    sqrt_parser.add_argument('a')

    return parser

def execute(args):
    command = args.command

    if command == 'add':
        result = b.add(args.a, args.b)
    elif command == 'subtract':
        result = b.subtract(args.a, args.b)
    elif command == 'multiply':
        result = b.multiply(args.a, args.b)
    elif command == 'divide':
        result = b.divide(args.a, args.b)
    elif command == 'power':
        result = adv.power(args.a, args.b)
    elif command == 'sqrt':
        result = adv.sqrt(args.a)
    else:
        raise ValueError("Unknown operation.")
    
    print(f"Result: {result}")
