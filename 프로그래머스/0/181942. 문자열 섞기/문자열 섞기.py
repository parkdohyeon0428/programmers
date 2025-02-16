def solution(str1, str2):
    result = "" # 변수 초기화 꼭 기억하기
    for i in range(0, len(str1)):
        
        result += str1[i] + str2[i]
    return result

