def main():
    tc = int(input())

    x = 0
    for _ in range(tc):
        cmd = input()

        if '++' in cmd:
            x += 1
        elif '--' in cmd:
            x -= 1
    
    print(x)

    
if __name__ == '__main__':
    main()