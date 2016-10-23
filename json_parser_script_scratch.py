import json, os

cwd = os.getcwd()
json_review_list = []
with open(os.path.join(cwd,'yelp_dataset_challenge_academic_dataset', 'yelp_academic_dataset_review.json')) as f:
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
# print(len(json_review_list))
# number_char = 0
with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'corpus'),'w') as f:
    for i in range(0,len(json_review_list)):
        if json_review_list[i]['type'] == 'review':
            text = json_review_list[i]['text']
            if text:
                try:
                    f.write(text)
                except:
                    pass
                    # number_char+=1
                    # print(i)
                    # print(text)
# print(number_char)
f.close()
