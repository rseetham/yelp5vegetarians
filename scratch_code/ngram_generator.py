import os, re

cwd = os.getcwd()
input_list = ['all', 'this', 'happened', 'more', 'or', 'less']
b = []
def find_ngrams():
    # cwd = os.getcwd()
    f = open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset','corpus_1useful_review.txt'))
    lines = f.flatMap(lambda line: re.sub('[^.a-zA-Z]', line).lower().split("."))
    for i in range(0,len(list(zip(*[lines[i:] for i in range(2)])))):
        s = ' '
        b.append(s.join(list(zip(*[lines[i:] for i in range(2)]))[i]))
    return b
f2 = open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset','corpus_bigrams_flatmap.txt'))
f2.write(str(find_ngrams()))
