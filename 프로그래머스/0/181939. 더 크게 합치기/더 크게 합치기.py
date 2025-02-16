def solution(c,d):
    result = max(int(f'{c}{d}'), int(f'{d}{c}'))
    return result

solution(1,2)