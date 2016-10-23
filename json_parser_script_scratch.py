import json, os

cwd = os.getcwd()
json_review_list = []
with open(os.path.join(cwd,'yelp_training_set','yelp_dataset_challenge_academic_dataset.json')) as f:
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
        json_review_list.append(jfile)
f.close()
with open(os.path.join(cwd, 'corpus'),'w') as f:
    for i in range(0,len(json_review_list)):
        if json_review_list[i]['type'] == 'review':
            text = json_review_list[i]['text']
            if text:
                f.write(text+'\n')
f.close()
