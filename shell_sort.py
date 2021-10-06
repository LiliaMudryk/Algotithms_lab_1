

import time

def shell_sort(lst):
    comparisons =0
    current_time = time.time_ns()
    gap = len(lst)//2
    while gap>0:
        for i in range(gap,len(lst)):
            temp = lst[i]
            j = i
            while  j >= gap and lst[j-gap] >temp:
                lst[j] = lst[j-gap]
                j -= gap
                comparisons+=1
            lst[j] = temp
            if j>=gap:
                comparisons+=1
        gap = gap//2
    runtime = time.time_ns()-current_time
    return lst,comparisons,runtime
