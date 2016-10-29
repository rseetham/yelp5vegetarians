import json, os, csv
cwd = os.getcwd()
rating_list = []
with open(os.path.join(cwd,'yelp_dataset_challenge_academic_dataset', 'corpus_1useful_review.json')) as f:
    jfile={}
    for line in f:
        while True:
            try:
                jfile = json.loads(line)
                break
            except ValueError:
                # Not yet a complete JSON value
                line += next(f)
        # do something with jfile
        if jfile:
            try:
           rating_list.append(jfile['stars'])
