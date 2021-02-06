def main():
    a, b, c, d = tuple(map(lambda x: int(x), input().split()))

    misha = max(3 * a / 10, a - a / 250 * c)
    vasya = max(3 * b / 10, b - b / 250 * d)

    if misha > vasya:
        print('Misha')
    elif vasya > misha:
        print('Vasya')
    else:
        print('Tie')

    
if __name__ == '__main__':
    main()