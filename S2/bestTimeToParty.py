sched = [(6, 8), (6, 12), (6, 7), (7, 8), (7, 10), (8, 9), (8, 10), (9, 12), (9, 10), (10, 11), (10, 12), (11, 12)]


def bestTimeToParty(schedule):
    start = schedule[0][0]
    end = schedule[0][1]
    for c in schedule:
        start = min(start, c[0])
        end = max(end, c[1])

    count = celebrityDensity(schedule, start, end)
    print(count)
    # maxcount = 0
    # for i in range(start, end + 1):
    #     if count[i] > maxcount:
    #         maxcount = count[i]
    #         time = i
    maxcount = max(count[start:end + 1])
    time = count.index(maxcount)
    print(f'Best time to attend the party is at {time} o\'clock : {maxcount} celebrities will be attending!')


def celebrityDensity(sched, start, end):
    count = [0] * (end + 1)
    for i in range(start, end + 1):
        count[i] = 0
        for c in sched:
            if c[0] <= i < c[1]:
                count[i] += 1
    return count


if __name__ == '__main__':
    bestTimeToParty(sched)
