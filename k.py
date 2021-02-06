def main():
    moves = input()

    for i, ch in enumerate(moves):
        if i % 2 == 0 and ch == 'L':
            print('No')
            quit(0)
        elif i % 2 == 1 and ch == 'R':
            print('No')
            quit(0)
    
    print('Yes')    

    
if __name__ == '__main__':
    main()