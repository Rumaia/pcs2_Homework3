class MinMaxBubble(object):

    def __init__(self):
        self.content = []

    def bubble_sort(self):
        for passnum in range(len(self.content)-1,0,-1):
            for i in range(passnum):
                if self.content[i]>self.content[i+1]:
                    temp = self.content[i]
                    self.content[i] = self.content[i+1]
                    self.content[i+1] = temp

    def add(self,value):
            self.content.append(value)
            self.bubble_sort()

    def get_min(self):
        return self.content[0]


    def get_max(self):
        return self.content[-1]

a = MinMaxBubble()
a.add(25)
a.add(27)
a.add(4)
a.add(10)
a.add(17)
print(a.get_max())
print(a.get_min())

import random
for r in range(100):
    num = random.randint(0,1000)
    a.add(num)
    my_min = a.get_min()
    my_max = a.get_max()

import time
def measure_time(a,rounds):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0

    for r in range(rounds):

        num = random.randint(0, 100)
        start = time.time()
        my_add = a.add(num)
        tot_time_add += (time.time() - start)

        start = time.time()
        my_min = a.get_min()
        tot_time_min += (time.time() - start)

        start = time.time()
        my_max = a.get_max()
        tot_time_max += (time.time() - start)

    tot_time_add /= rounds
    tot_time_min /= rounds      ### doing the average by dividing by the number of rounds. so that we can the time needed for 1 round
    tot_time_max /= rounds

    return tot_time_add, tot_time_min, tot_time_max

for rounds in range(100,500,100):
    print(rounds, measure_time(a,rounds))

values_add, values_min, values_max = [], [], []
for rounds in range(100,500,100):
    a= MinMaxBubble()
    my_add, my_min, my_max = measure_time(a, rounds)
    values_add.append(my_add * 1000)
    values_min.append(my_min * 1000)
    values_max.append(my_max * 1000)

import matplotlib.pyplot as plt
xlabels = range(100,500,100)
plt.plot(xlabels, values_add, label='add')
plt.plot(xlabels, values_min, label='get_min')
plt.plot(xlabels, values_max, label='get_max')
plt.legend()
plt.xlabel('Number of Operations')
plt.ylabel('Execution Time(msec)')
plt.title('Performance')
plt.show()

