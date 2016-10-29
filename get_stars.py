import json, os, csv
cwd = os.getcwd()
json_review_list = []

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'dataset_1usefulreview_review_refiltered.json')) as f:
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
            json_review_list.append(jfile)
countratings = []
ratingscsv = open(os.path.join(cwd, 'ratings.csv'), 'w')
count = 0
othercount = 0
for i in range(0,len(json_review_list)):
    if json_review_list[i]['type'] == 'review':
        stars = json_review_list[i]['stars']
        if stars:
            try:
                ratingscsv.write(stars+'\n')
                countratings.append(stars)
                othercount+=1
                if othercount < 5:
                    print(str(json_review_list[i]+'\n'))
            except:
                count +=1
# print(count) #26
print(othercount) # 809680
print(len(countratings))
# print(countratings)
ratingscsv.close()
f.close()
# print()