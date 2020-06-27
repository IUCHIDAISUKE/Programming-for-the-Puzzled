sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]
sched2 = [(6.0, 8.0), (6.5, 12.0), (6.5, 7.0), (7.0, 8.0), (7.5, 10.0), (8.0, 9.0), (8.0, 10.0), (9.0, 12.0),
          (9.5, 10.0), (10.0, 11.0), (10.0, 12.0), (11.0, 12.0)]


def bestTimeToPartySmart2(schedule):
    ans = time = 0
    for target in schedule:
        cnt = 0
        for other in schedule:
            if other[0] <= target[0] < other[1]:
                cnt += 1
        # print(target)
        # print(cnt)
        if ans < cnt:
            time = target[0]
            ans = cnt

    print(f'Best time to attend the party is at {time} o\'clock : {ans} celebrities will be attending!')


if __name__ == '__main__':
    bestTimeToPartySmart2(sched2)
