import json, os, csv
cwd = os.getcwd()

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'corpus_1useful_review.txt')) as f:
    head = [next(f) for x in range(20)]
print(head)