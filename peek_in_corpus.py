import json, os, csv
cwd = os.getcwd()

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'corpus_1useful_review.txt')) as f:
    head = [next(f) for x in range(2)]
print(head)

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'dataset_1usefulreview_review_refiltered.json')) as f:
    head = [next(f) for y in range(2)]
print(head)