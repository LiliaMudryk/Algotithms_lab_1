
from insetrion_sort import insertion_sort
import time
from merge_sort import merge_sort
from selection_sort import selection_sort
from shell_sort import shell_sort
from list_generator import generate_decreasing, generate_increasing, generate_random, generate_small_range
import matplotlib.pyplot as plt
sotring_algorithms = [insertion_sort,selection_sort,merge_sort,shell_sort]
# experiments_names = ['RANDOM','INCREASING','DECREASING','REPEATED']
# experiment_lists = [generate_random,generate_increasing,generate_decreasing,generate_small_range]
# x = [7,8,9,10,11,12,13,14,15]

def experiment_1(algorithm):
    lst_power = 7
    # time = 0
    # comparisons = 0
    result = []
    while lst_power<=15:
        time = 0
        comparisons = 0
        for i in range(5):
                lst = generate_random(lst_power)
                sorted = algorithm(lst)
                time+= sorted[2]
                comparisons+=sorted[1]
        result.append((round(comparisons/5),time/5))
        lst_power+=1
    print(result)
    name = 'Random array'
    return result,name
def experiment_2(algorithm):
    lst_power = 7
    result = []

    while lst_power<=15:
        lst = generate_increasing(lst_power)
        sorted = algorithm(lst)
        time = sorted[2]
        comparisons =sorted[1]
        result.append((comparisons,time))
        lst_power+=1
    print(result)
    name = 'Increasing array'
    return result,name
def experiment_3(algorithm):
    lst_power = 7
    result = []
    while lst_power<=15:


        lst = generate_decreasing(lst_power)
        sorted = algorithm(lst)
        time = sorted[2]
        comparisons =sorted[1]
        result.append((comparisons,time))
        lst_power+=1
    print(result)
    name = 'Decreasing array'
    return result,name
def experiment_4(algorithm):
    lst_power = 7

    result = []
    while lst_power<=15:
        time = 0
        comparisons = 0
        for i in range(3):
                lst = generate_small_range(lst_power)
                sorted = algorithm(lst)
                time+= sorted[2]
                comparisons+=sorted[1]
        result.append((round(comparisons/3),time/3))
        lst_power+=1
    print(result)
    name = 'Repeated array'
    return result,name
def save_graph(experiment):
        x = [7,8,9,10,11,12,13,14,15]
        y1 = []
        for i in experiment[0][0]:
            y1.append(i[1])
        plt.plot(x, y1, color = 'r',label = 'Insertion sort')


        y2 =[]
        for i in experiment[1][0]:
            y2.append(i[1])
        plt.plot(x, y2, color = 'y',label = 'Selection sort')

        y3 =[]
        for i in experiment[2][0]:
            y3.append(i[1])
        plt.plot(x, y3, color = 'b',label = 'Merge sort')

        y4 =[]
        for i in experiment[3][0]:
            y4.append(i[1])
        plt.plot(x, y4, color = 'g',label = 'Shell sort')
        plt.legend()
        plt.yscale('log')
        plt.ylabel("Time")
        plt.title(experiment[0][1])
        plt.savefig(experiment[0][1]+' experiment(time)')
        plt.close()





        y1 = []
        for i in experiment[0][0]:
            y1.append(i[0])
        plt.plot(x, y1, color = 'r',label = 'Insertion sort')


        y2 =[]
        for i in experiment[1][0]:
            y2.append(i[0])
        plt.plot(x, y2, color = 'y',label = 'Selection sort')

        y3 =[]
        for i in experiment[2][0]:
            y3.append(i[0])
        plt.plot(x, y3, color = 'b',label = 'Merge sort')

        y4 =[]
        for i in experiment[3][0]:
            y4.append(i[0])
        # print(x)
        plt.plot(x, y4, color = 'g',label = 'Shell sort')
        plt.legend()
        plt.ylabel("Comparisons")
        plt.yscale('log')
        plt.title(experiment[0][1])
        plt.savefig(experiment[0][1]+' experiment(comparisons)')
        plt.close()


# save_graph([experiment_1(insertion_sort),experiment_1(selection_sort),experiment_1(merge_sort),experiment_1(shell_sort)])
save_graph([experiment_1(i) for i in sotring_algorithms])
save_graph([experiment_2(i) for i in sotring_algorithms])
save_graph([experiment_3(i) for i in sotring_algorithms])
save_graph([experiment_4(i) for i in sotring_algorithms])

# save_graph(experiment_3(insertion_sort),experiment_3(selection_sort),experiment_3(merge_sort),experiment_3(shell_sort))
