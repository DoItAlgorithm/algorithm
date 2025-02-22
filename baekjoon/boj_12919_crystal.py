S,T = input(), input()

result = 0
def dfs(cur_chars):
    global result
    if result :
        return

    if len(cur_chars) == len(S):
        if cur_chars == S:
            result = 1
        return

    if cur_chars[-1] == 'A':
        #print(f'A : {cur_chars[:-1]}')
        dfs(cur_chars[:-1])

    if cur_chars[0] == 'B':
        #print(f'B : {cur_chars[1:][::-1]}')
        dfs(cur_chars[1:][::-1])


dfs(T)
print(result)