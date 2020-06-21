import numpy as np
import statistics as stats

empty_counts = np.load('empty_counts.npy')
empty_firsts = np.load('empty_firsts.npy')
empty_lasts = np.load('empty_lasts.npy')


        
for j in range(len(empty_counts[0])):
    sum = 0
    total = 0
    for i in range(len(empty_counts)):
        total += 121
        sum += empty_counts[i][j]
    print(sum)
    print(total)
    print(sum / total * 100)

print(empty_firsts)
print(empty_lasts)

for j in range(len(empty_firsts[0])):
    #print(j)
    vals = []
    for i in range(len(empty_firsts)):
        if(empty_firsts[i][j] > 0):
            vals.append(empty_firsts[i][j])
    #print(stats.stdev(vals))
    print(stats.mean(vals), "±", round(stats.stdev(vals),4))
    #print()

for j in range(len(empty_lasts[0])):
    #print(j)
    vals = []
    for i in range(len(empty_lasts)):
        if(empty_lasts[i][j] > 0):
            vals.append(empty_lasts[i][j])
    print(stats.mean(vals), "±", round(stats.stdev(vals),4))
    #print()

empty_diff = [[0] * len(empty_counts[0]) for i in range(len(empty_counts))]
empty_diff = np.array(empty_diff)
print(empty_diff)
print(empty_counts)

for i in range(len(empty_diff)):
    for j in range(len(empty_diff[0])):
        if(empty_firsts[i][j] == -1):
            empty_diff[i][j] = 0
        else:
            empty_diff[i][j] = empty_lasts[i][j] - empty_firsts[i][j] + 1
print(empty_diff)

empty_cp = [[0.0] * len(empty_counts[0]) for i in range(len(empty_counts))]
empty_cp = np.array(empty_cp)
print(empty_cp)

for i in range(len(empty_cp)):
    for j in range(len(empty_cp[0])):
        if(empty_diff[i][j] == 0):
            empty_cp[i][j] = 0
        else:
            empty_cp[i][j] = empty_counts[i][j] / empty_diff[i][j]
    #print(empty_cp[i][j])
print(empty_cp)

for j in range(len(empty_cp[0])):
    print(j)
    vals = []
    for i in range(len(empty_cp)):
        if(empty_cp[i][j] > 0):
            vals.append(empty_cp[i][j])
    print(stats.mean(vals), "±", round(stats.stdev(vals),4))
    #print()