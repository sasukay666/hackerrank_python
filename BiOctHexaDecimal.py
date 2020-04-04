# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    '''This function can be used to print the decimal, octal, hexadecimal and
    binary value of integers upto the input decimal number, side by side.
    syntax: print_formatted(int)'''
    n = len(bin(number))-2
    for i in range(1, number+1):
        print(f'{i}'.rjust(n), oct(i)[2:].rjust(n), hex(i)[2:].upper().rjust(n), bin(i)[2:].rjust(n))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
