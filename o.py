def main():
    t = int(input())

    feelings = ['I hate' if i % 2 == 0 else 'I love' for i in range(t)]
    
    print(' that '.join(feelings), 'it')
    
    
    
if __name__ == '__main__':
    main()