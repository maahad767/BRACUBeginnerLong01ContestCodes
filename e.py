def main():
    sentence = input().replace(".", '').replace(',', '').replace('!', '').replace('?', '').replace(' ', '')

    while sentence != 'DONE':
        print("You won't be eaten!" if sentence.lower() == sentence[::-1].lower() else "Uh oh..")
        sentence = input().replace(".", '').replace(',', '').replace('!', '').replace('?', '').replace(' ', '')

if __name__ == '__main__':
    main()