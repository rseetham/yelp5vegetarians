import os, csv
import matplotlib.pyplot as plt

cwd = os.getcwd()

wordcount_list = []
frequency_list = []
frequency_list_t = []
frequency_list_t2 = []
with open(os.path.join(cwd, 'corpus_2.csv'), 'r') as f:
    reader = csv.reader(f)
    wordfreq_list = list(reader)
    for line in wordfreq_list:
        line[1] = int(line[1])
        wordcount_list.append(addition)
        frequency_list.append(addition[1])
        if addition[1]>100:
            frequency_list_t.append(addition[1])
        if addition[1]>100000:
            frequency_list_t2.append(addition[1])
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
plt.hist(frequency_list,bins=50)
plt.xticks(rotation=20)
f.savefig(os.path.join(cwd, 'frequency_hist'))

g = plt.figure(2)
plt.hist(frequency_list_t,bins=range(100,9179998,179998))
plt.xticks(range(100,9179998,1799980),rotation=20)

g.savefig(os.path.join(cwd, 'truncated100_frequency_hist'))

h = plt.figure(3)
plt.hist(frequency_list_t2,bins=range(100000, 9089000,89000))
plt.xticks(range(100000, 9089000,890000),rotation=20)
h.savefig(os.path.join(cwd, 'truncated100000_frequency_hist'))

