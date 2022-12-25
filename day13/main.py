#%%
import functools


input_ = [row.strip('\n') for row in open('mission.txt').readlines()]

input = []
for row in input_:
    if row != '':
        input.append(eval(row))

def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

def compare(left, right):
    match left, right:
        case int(), int():
            return left - right
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])
        case list(), list():
            for l, r in zip(left, right):
                if diff := compare(l, r):
                    return diff
            else:
                return len(left) - len(right)

silver = []
for idx, row in enumerate(pairwise(input), start=1):
    cmp = compare(row[0], row[1])
    if cmp < 0:
        silver.append(idx)

#%%
print(sum(silver))

#%%
# Gold
packets = [[[2]], [[6]]]
for idx, row in enumerate(pairwise(input), start=1):
    packets += [row[0], row[1]]

input_sorted = sorted(packets, key=functools.cmp_to_key(compare))
print((1 + input_sorted.index([[2]])) * (1 + input_sorted.index([[6]])))
