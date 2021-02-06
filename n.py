def main():
    tc = int(input())

    for _ in range(tc):
        num = int(input())
        
        neg_sum = 0
        i = 1
        while i <= num:
            neg_sum += i
            i = i * 2

        possum = num * (num + 1) // 2
        print(possum - neg_sum * 2)
        
    
if __name__ == '__main__':
    main()