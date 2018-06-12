def quick_sort(x, start, end):
    if start >= end:
        return
    i = start
    j = end
    key = x[start]
    while i < j:
        while i < j and x[j] >= key:
            j -= 1
        x[i] = x[j]
        while i < j and x[i] <= key:
            i += 1
        x[j] = x[i]
    x[i] = key
    quick_sort(x, start, i-1)
    quick_sort(x, i+1, end)


if __name__ == '__main__':
    from random import randint
    x = [randint(1, 100) for i in range(80)]
    quick_sort(x, 0, len(x)-1)
    print(x)