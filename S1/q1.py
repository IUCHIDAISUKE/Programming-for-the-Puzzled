cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
cap3 = ['F', 'F', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']


def pleaseConform(caps):
    start = forward = backward = 0
    intervals = []
    for i in range(len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i - 1, caps[i - 1]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    intervals.append((start, len(caps) - 1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'
    for t in intervals:
        if t[2] == flip:
            if t[1] - t[0] == 0:
                print(f'People at positions {t[0]} flip your caps!.')
            else:
                print(f'People in positions {t[0]} through {t[1]} flip your caps!.')


if __name__ == '__main__':
    pleaseConform(cap1)
    print()
    pleaseConform(cap2)
    print()
    pleaseConform(cap3)
