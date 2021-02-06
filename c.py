def main():
    tc = int(input())
    exercises = {
        "chest" : 0,
        "biceps" : 0,
        "back" : 0,
    }
    times = list(map(lambda x: int(x), input().split()))
    for i, t in enumerate(times):
        if i % 3 == 0:
            exercises['chest'] += t
        elif i % 3 == 1:
            exercises['biceps'] += t
        else:
            exercises['back'] += t
    
    maxexercise = max(exercises, key=exercises.get) 
    print(maxexercise)


if __name__ == '__main__':
    main()