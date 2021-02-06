def main():
    total = int(input())
    
    orange_juices = list(map(lambda x: int(x), input().split()))

    print(sum(orange_juices) / total)

    
if __name__ == '__main__':
    main()