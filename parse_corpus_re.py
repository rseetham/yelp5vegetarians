import os
import matplotlib.pyplot as plt

cwd = os.getcwd()

wordcount_list = []
frequency_list = []
frequency_list_t = []
with open(os.path.join(cwd, 'corpus_re.txt'), 'r') as f:
    for line in f:
        addition = line.split()
        addition[1] = int(addition[1])
        wordcount_list.append(addition)
        frequency_list.append(addition[1])
        if addition[1]>100:
            frequency_list_t.append(addition[1])
f.close()
wordcount_list.sort(reverse=True, key=lambda x: x[1])
output_wc = open(os.path.join(cwd, 'sorted_wc.txt'), 'w')
output_wc2 = open(os.path.join(cwd, 'sorted_wc2.txt'), 'w')
output_wc2t = open(os.path.join(cwd, 'sorted_wc2_truncated.txt'), 'w')
for i in wordcount_list:
    output_wc.write(str(i) + '\n')
    output_wc2.write(i[0]+','+str(i[1])+'\n')
    if i[1]>100:
        output_wc2t.write(i[0]+','+str(i[1])+'\n')
output_wc.close()
output_wc2.close()
output_wc2t.close()
f = plt.figure(1)
plt.hist(frequency_list,bins=500)
f.savefig(os.path.join(cwd, 'frequency_hist'))
g = plt.figure(2)
plt.hist(frequency_list_t,bins=500)
g.savefig(os.path.join(cwd, 'truncated_frequency_hist'))

