import sys
import math

def main():
    lines = sys.stdin.readlines()
    numstr = " ".join(lines)
    numbers = numstr.split()

    for number in numbers[::-1]:
        print('%.4f'% round(math.sqrt(int(number)), 4))

    
if __name__ == '__main__':
    main()