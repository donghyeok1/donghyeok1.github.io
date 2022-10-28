import heapq
def solution(jobs):
    answer = 0
    q = []
    temp = []
    time = 0
    for i in jobs:
        heapq.heappush(q, (i[0], i[1]))
    a, b = heapq.heappop(q)
    heapq.heappush(temp, (b, a))
    while q:
        while True:
            if len(q) != 0:
                a, b = heapq.heappop(q)
                if a <= time:
                    heapq.heappush(temp, (b, a))
                else:
                    heapq.heappush(q, (a, b))
                    if len(temp) != 0:
                        c, d = heapq.heappop(temp)
                        t = time + c - d
                        answer += t
                        time += c
                        break
                    else:
                        time += 1 
            else:
                for i in range(len(temp)):
                    c, d = heapq.heappop(temp)
                    t = time + c - d
                    answer += t
                    time += c
                break
        
    return answer // len(jobs)

print(solution([[0,16],[0,14],[15,1],[13,13]]))