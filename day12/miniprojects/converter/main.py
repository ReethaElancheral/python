# converter/main.py

import argparse
from converter.length import meters, kilometers
from converter.weight import grams, kilograms
from converter.temperature import celsius, fahrenheit

def main():
    parser = argparse.ArgumentParser(description="Unit Converter")

    subparsers = parser.add_subparsers(dest="category", help="Conversion categories")

    # Length conversions
    length_parser = subparsers.add_parser("length", help="Length conversions")
    length_subparsers = length_parser.add_subparsers(dest="unit", help="Length units")

    length_subparsers.add_parser("meters-to-kilometers", help="Convert meters to kilometers")
    length_subparsers.add_parser("meters-to-miles", help="Convert meters to miles")
    length_subparsers.add_parser("kilometers-to-meters", help="Convert kilometers to meters")
    length_subparsers.add_parser("kilometers-to-miles", help="Convert kilometers to miles")

    # Weight conversions
    weight_parser = subparsers.add_parser("weight", help="Weight conversions")
    weight_subparsers = weight_parser.add_subparsers(dest="unit", help="Weight units")

    weight_subparsers.add_parser("grams-to-kilograms", help="Convert grams to kilograms")
    weight_subparsers.add_parser("grams-to-pounds", help="Convert grams to pounds")
    weight_subparsers.add_parser("kilograms-to-grams", help="Convert kilograms to grams")
    weight_subparsers.add_parser("kilograms-to-pounds", help="Convert kilograms to pounds")

    # Temperature conversions
    temp_parser = subparsers.add_parser("temperature", help="Temperature conversions")
    temp_subparsers = temp_parser.add_subparsers(dest="unit", help="Temperature units")

    temp_subparsers.add_parser("celsius-to-fahrenheit", help="Convert Celsius to Fahrenheit")
    temp_subparsers.add_parser("celsius-to-kelvin", help="Convert Celsius to Kelvin")
    temp_subparsers.add_parser("fahrenheit-to-celsius", help="Convert Fahrenheit to Celsius")
    temp_subparsers.add_parser("fahrenheit-to-kelvin", help="Convert Fahrenheit to Kelvin")

    args = parser.parse_args()

    if args.category == "length":
        value = float(input("Enter value: "))
        if args.unit == "meters-to-kilometers":
            print(meters.to_kilometers(value))
        elif args.unit == "meters-to-miles":
            print(meters.to_miles(value))
        elif args.unit == "kilometers-to-meters":
            print(kilometers.to_meters(value))
        elif args.unit == "kilometers-to-miles":
            print(kilometers.to_miles(value))
    elif args.category == "weight":
        value = float(input("Enter value: "))
        if args.unit == "grams-to-kilograms":
            print(grams.to_kilograms(value))
        elif args.unit == "grams-to-pounds":
            print(grams.to_pounds(value))
        elif args.unit == "kilograms-to-grams":
            print(kilograms.to_grams(value))
        elif args.unit == "kilograms-to-pounds":
            print(kilograms.to_pounds(value))
    elif args.category == "temperature":
        value = float(input("Enter value: "))
        if args.unit == "celsius-to-fahrenheit":
            print(celsius.to_fahrenheit(value))
        elif args.unit == "celsius-to-kelvin":
            print(celsius.to_kelvin(value))
        elif args.unit == "fahrenheit-to-celsius":
            print(fahrenheit.to_celsius(value))
        elif args.unit == "fahrenheit-to-kelvin":
            print(fahrenheit.to_kelvin(value))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
