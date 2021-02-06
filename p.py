import math


def main():
    n, m = map(lambda x: int(x), input().split())
    puzzles = sorted(list(map(lambda x: int(x), input().split())))

    min_diff = math.inf
    
    for i in range(len(puzzles) - n + 1):
        chosen = puzzles[i:i + n]
        diff = max(chosen) - min(chosen)
        
        if diff < min_diff: 
            min_diff = diff
        
    print(min_diff)

    
if __name__ == '__main__':
    main()