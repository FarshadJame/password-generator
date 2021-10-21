import string
import random
import argparse


def generate_password(length, upper=False, lower=False, digits=False):
    password = ''
    if upper:
        password += string.ascii_uppercase

    if lower:
        password += string.ascii_lowercase

    if digits:
        password += string.digits

    if password == '':
        password += string.ascii_letters + str(string.digits)

    print(''.join(random.sample(password, k=length)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("length", help="Length of password", type=int)
    parser.add_argument("-u", "--upper", help="Add uppercase letters to string of password", action="store_true")
    parser.add_argument("-l", "--lower", help="Add lowercase letters to string of password", action="store_true")
    parser.add_argument("-d", "--digits", help="Add digits to string of password", action="store_true")
    args = parser.parse_args()
    generate_password(args.length, args.upper, args.lower, args.digits)
