class MinMaxClassQuick(object):
    def __init__(self):
        self.content=[]
        self.size = 0

    def add(self,value):
        self.content.append(value)
        self.size += 1

    def quickSort(self):
        if len(self.content) > 1:
            piv = self.content[0]
            self.left = MinMaxClassQuick()
            self.right =MinMaxClassQuick()
            for i in range(1, len(self.content)):
                if (self.content[i] < piv):
                    self.left.add(self.content[i])

                else:
                    self.right.add(self.content[i])
            return self.left.quickSort() + [piv] + self.right.quickSort()

        else:
            return self.content

    def get_min(self):
        new = self.quickSort()
        return new[0]

    def get_max(self):
        new = self.quickSort()
        leng = self.size -1
        return new[leng]

    def get_list(self):
        return self.content




a = MinMaxClassQuick()
a.add(2)
a.add(5)
a.add(7)
print(a.get_min())
print(a.get_max())
print(a.quickSort())
print(a.content)


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
    a= MinMaxClassQuick()
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




