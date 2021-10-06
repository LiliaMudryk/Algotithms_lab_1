
import time


def merge_sort(lst: list):
    counter = 0
    current = time.time_ns()
    if len(lst) > 1:
        mid = len(lst) // 2
        l = lst[:mid]
        r = lst[mid:]

        counter += merge_sort(l)[1]
        counter += merge_sort(r)[1]

        i = 0
        j = 0
        k = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                lst[k] = l[i]
                i += 1
            else:
                lst[k] = r[j]
                j += 1
            counter += 1
            k += 1

        while i < len(l):
            lst[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            lst[k] = r[j]
            j += 1
            k += 1
    runtime = time.time_ns()-current
    return lst, counter,runtime
