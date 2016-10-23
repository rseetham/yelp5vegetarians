import os

cwd = os.getcwd()

wordcount_list = []
with open(os.path.join(cwd, 'corpus_re.txt'), 'r') as f:
    for line in f:
        addition = line.split()
        addition[1] = int(addition[1])
        wordcount_list.append(addition)
f.close()
wordcount_list.sort(reverse=True, key=lambda x: x[1])
output_wc = open(os.path.join(cwd, 'sorted_wc.txt'), 'w')
for i in wordcount_list:
    output_wc.write(str(i)+'\n')
output_wc.close()
