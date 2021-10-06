import random
def generate_random(lst_power):
    lst = []
    while len(lst)<2**lst_power:
        lst.append(random.randint(0,2**18))
    return lst
def generate_increasing(lst_power):
    lst = []
    i=1
    while len(lst)<2**lst_power:
        lst.append(i)
        i+=1
    return lst
def generate_decreasing(lst_power):
    lst = []
    i=2**18
    while len(lst)<2**lst_power:
        lst.append(i)
        i-=1
    return lst
def generate_small_range(lst_power):
    lst = []
    while len(lst)<2**lst_power:
        i = random.randint(1,3)
        lst.append(i)

    return lst
