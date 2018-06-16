from random import randint
from quick_sort import quick_sort


def partition(x, l, r, i):
    x[i], x[r] = x[r], x[i]
    pivot = x[r]
    m = l
    for n in range(l, r):
        if x[n] <= pivot:
            x[m], x[n] = x[n], x[m]
            m += 1
    x[m], x[r] = x[r], x[m]
    return m

def quick_select(x, l, r, k):
    if l == r:
        return x[l]
    while True:
        i = randint(l, r)
        m = partition(x, l, r, i)
        n = m - l + 1
        if k == n:
            return x[m]
        elif k < n:
            r = m - 1
        else:
            k -= n
            l = m + 1


if __name__ == '__main__':
    x = [randint(1, 1000) for i in range(80)]
    l = 0
    r = len(x) - 1
    k = 6

    print(quick_select(x, l, r, k))
    
    quick_sort(x, l, r)
    print(x[k-1])
