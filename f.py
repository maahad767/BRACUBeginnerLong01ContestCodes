def main():
    length = int(input())
    numbers = list(map(lambda n: int(n), input().split()))

    i, c = 1, 0
    while i < length - 1:
        c += 1 if numbers[i-1] < numbers[i] < numbers[i+1] or numbers[i-1] > numbers[i] > numbers[i+1]  else 0
        i += 1

    print(c)


if __name__ == '__main__':
    main()