import argparse
import random
import string


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-lc', help='lines count', type=int, default=30000)
    parser.add_argument('-ls', help='line sep', type=str, default="\n")
    parser.add_argument('-fs', help='field sep', type=str, default="\t")
    parser.add_argument('-fc', help='fields count', type=int, default=6)
    parser.add_argument('-fsz', help='field size', type=int, default=10)
    parser.add_argument('-f', help='file', type=str, default="input.txt")
    parser.add_argument('-v', help="variable amount of fields in string", action="store_true")
    parser.add_argument('-d', help="digits only", action="store_true")

    return parser.parse_args()


def field_generator(max_chars=6, chars=string.ascii_lowercase, var=False):
    if var:
        return "".join(random.choice(chars) for _ in range(random.randint(1, max_chars)))
    else:
        return "".join(random.choice(chars) for _ in range(max_chars))


def string_generator(args):
    output = ""

    for line in range(args.lc):
        for field in range(args.fc):
            if args.d:
                output += field_generator(max_chars=args.fsz, chars=string.digits, var=args.v)
            else:
                output += field_generator(max_chars=args.fsz, var=args.v)

            if field != args.fc-1:
                output += args.fs

        if line != args.lc-1:
            output += args.ls

    return output


def main():
    args = parse_args()

    print("Generation params: ")
    print("\tFile: " + args.f)
    print("\tLines count: " + str(args.lc))
    print("\tOnly digits: " + str(args.d))
    print("\tVariable field size: " + str(args.v))
    print("\tField size: " + str(args.fsz))
    print("\tFields in line: " + str(args.fc))

    file = open(args.f, "w")
    file.write(string_generator(args))

    print("\nGeneration completed!")
    print("File size: " + str(round(len(open(args.f).read())/1000)) + " KB")


if __name__ == "__main__":
    main()