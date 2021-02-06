def main():
    a, b = tuple(map(lambda n: int(n), input().split()))

    max_coin = 0
    if a != b:
        max_coin = max(a, b) * 2 - 1
    else:
        max_coin = a + b

    print(max_coin)

    
if __name__ == '__main__':
    main()