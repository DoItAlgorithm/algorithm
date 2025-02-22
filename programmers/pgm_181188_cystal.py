def solution(targets):
    result = 0
    pre_end_point = 0
    targets.sort(key=lambda x : x[1])

    for s,e in targets:
        if s >= pre_end_point :
            result += 1
            pre_end_point = e

    return result
