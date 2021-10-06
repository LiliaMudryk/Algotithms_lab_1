
import time
def selection_sort(lst):
    comparisons =0
    current_time=time.time_ns()
    for i in range(0,len(lst)):
        min = i
        for j in range(i+1,len(lst)):
          comparisons+=1
          if lst[min]>lst[j]:
            min = j
        if min !=i:
            lst[min],lst[i] = lst[i],lst[min]
    runtime = time.time_ns()-current_time
    return lst,comparisons,runtime

