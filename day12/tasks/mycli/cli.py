import argparse
from .core import run

def main():
    parser = argparse.ArgumentParser(...)
    parser.add_argument("--name")
    args = parser.parse_args()
    run(args.name)

if __name__ == "__main__":
    main()
