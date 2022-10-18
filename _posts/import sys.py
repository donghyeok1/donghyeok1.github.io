import sys

def solution(s):
    stack = []
    ans = list()
    index = 10000
    for j in range(1, len(s) + 1):
        if j == 1:
            stack.append(s[0])
            for i in range(1, len(s)):
                if stack[-1] == s[i]:
                    stack.append(s[i])
                    if i == len(s) - 1:
                        if len(stack) == 1:
                            a = str(stack[-1])
                        else:
                            a = str(len(stack)) + str(stack[-1])
                        ans += list(map("".join, a))
                else:
                    if len(stack) == 1:
                        a = str(stack[-1])
                    else:
                        a = str(len(stack)) + str(stack[-1])
                    stack.clear()
                    stack.append(s[i])
                    if i == len(s) - 1:
                        a += stack[-1]
                    ans += list(map("".join, a))
            min = len(ans)
        else:
            stack.append(s[ : j])
            for i in range(j, len(s)):
                if index == 10000:
                    if i + j > len(s):
                        if len(stack) == 1:
                            a = str(stack[-1]) + s[i : ]
                        else:
                            a = str(len(stack)) + str(stack[-1]) + s[i : ]
                        ans += list(map("".join, a))
                        break
                    elif stack[-1] == s[i : i + j]:
                        stack.append(stack[-1])
                        index = i + j
                    else:
                        if len(stack) == 1:
                            a = str(stack[-1])
                        else:
                            a = str(len(stack)) + str(stack[-1])
                        stack.clear()
                        stack.append(s[i : i + j])
                        index = i + j
                        ans += list(map("".join, a))
                else:
                    if index != i + 1:
                        continue
                    else:
                        index = 10000
            if len(stack) == 1:
                ans += list(map("".join, stack[-1]))
            elif len(stack) != 0:
                a = str(len(stack)) + str(stack[-1])
                ans += list(map("".join, a))
            if min > len(ans):
                min = len(ans)

        stack.clear()
        ans = list()

    return min

s = sys.stdin.readline().rstrip()

solution(s)