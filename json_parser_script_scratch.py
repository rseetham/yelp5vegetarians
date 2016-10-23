import json, os, csv
cwd = os.getcwd()
json_review_list = []
json_businessid_list = []
json_business_list = []

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'categories.csv'), 'r') as f:
    reader = csv.reader(f)
    categories_list = list(reader)
f.close()

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'yelp_academic_dataset_business.json')) as f:
    with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'truncated_businessid.csv'), 'w') as fw:
        jfile = {}
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
                categories_set = {elem for elem in jfile['categories']}
                # print(categories_set)
                categories_list_set = {elem for elem in categories_list[0]}
                # print(categories_list_set)
                if not categories_set.isdisjoint(categories_list_set):
                    json_businessid_list.append(jfile['business_id'])
                    json_business_list.append(jfile)
                    fw.write(jfile['business_id']+',')
f.close()
fw.close()

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
        if jfile:
            if jfile['business_id'] in json_businessid_list:
                json_review_list.append(jfile)
f.close()
fw.close()

print(len(json_review_list))

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'corpus'),'w') as f:
    with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'truncated_UserId_list.csv'), 'w') as fw:
        for i in range(0,len(json_review_list)):
            if json_review_list[i]['type'] == 'review':
                text = json_review_list[i]['text']
                if text:
                    try:
                        f.write(text)
                        fw.write(json_review_list[i]['user_id']+',')
                    except:
                        pass
f.close()
fw.close()
