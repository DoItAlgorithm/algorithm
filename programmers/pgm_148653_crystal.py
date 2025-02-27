def solution(storey):
    answer = 0
    while storey:
        rest = storey % 10   #나머지

        if rest <= 4:
            answer += rest

        elif rest >= 6:
            answer += (10-rest)
            storey += 10

        else: # 5일 때 (올림, 반올림 선택은 그 앞자리에 따라)
            if((storey // 10) % 10) >= 5:
                storey += 10
            answer += rest

        storey //= 10
    return answer
