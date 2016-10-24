input_list = ['all', 'this', 'happened', 'more', 'or', 'less']
b = []
def find_ngrams(input_list, n):
    for i in range(0,len(list(zip(*[input_list[i:] for i in range(n)])))):
        s = ' '
        b.append(s.join(list(zip(*[input_list[i:] for i in range(n)]))[i]))
    return b

find_ngrams(input_list,2)