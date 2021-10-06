import time
def insertion_sort(lst):
    comparisons = 0
    current_time = time.time_ns()
    for i in range(1,len(lst)):
        key = lst[i]
        j = i-1
        
        while j>=0 and lst[j]>key:
                comparisons+=1
                lst[j+1] = lst[j]
                j = j-1
        lst[j+1]= key
        if j !=-1:
            comparisons+=1
    runtime = time.time_ns()-current_time
    return lst,comparisons,runtime

