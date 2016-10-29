import json, os, csv
cwd = os.getcwd()
json_review_list = []
json_businessid_list = []
json_business_list = []

with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'categories.csv'), 'r') as f:
    reader = csv.reader(f)
    restaurant_categories_list = list(reader)
    # print(restaurant_categories_list[0])
    restaurant_categories_set = set()
    for restaurantcategory in restaurant_categories_list[0]:
        restaurant_categories_set.add(restaurantcategory)

f.close()

businessIDcsv = open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'businessID2.csv'),'w')
with open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'yelp_academic_dataset_business.json')) as f:
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
            categories_list = jfile['categories']
            categories_set = set(categories_list)
            # for category in categories_list:
            #     categories_set.add(category)
            if (not restaurant_categories_set.isdisjoint(categories_set)) and (jfile['business_id'] not in json_businessid_list):
                json_businessid_list.append(jfile['business_id'])
                businessIDcsv.write(jfile['business_id']+'\n')
f.close()
businessIDcsv.close()

newdataset = open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'dataset_1usefulreview_review.json'),'w')
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
            if jfile['business_id'] in json_businessid_list and (jfile['votes']['useful'] >= 1):
                try:
                    newdataset.write(str(jfile)+'\n')
                    json_review_list.append(jfile)
                except:
                    pass
f.close()
newdataset.close()

# print(len(json_review_list)) # 809706
countratings = []
newdataset2 = open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'dataset_1usefulreview_review_refiltered.json'),'w')
corpus = open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'corpus_1useful_review'),'w')
useridcsv = open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'truncated_UserId_list2.csv'), 'w')
ratingscsv = open(os.path.join(cwd, 'yelp_dataset_challenge_academic_dataset', 'ratings.csv'), 'w')
count = 0
othercount = 0
for i in range(0,len(json_review_list)):
    if json_review_list[i]['type'] == 'review':
        text = json_review_list[i]['text']
        if text:
            try:
                corpus.write(text+'\n')
                useridcsv.write(json_review_list[i]['user_id']+'\n')
                newdataset2.write(str(json_review_list[i])+'\n')
                countratings.append(json_review_list[i]['stars'])
                ratingscsv.write(json_review_list[i]['stars'])
                othercount+=1
                if othercount < 5:
                    print(str(json_review_list[i]+'\n'))
            except:
                count +=1
# print(count) #26
print(othercount) # 809680
print(len(countratings))
# print(countratings)
corpus.close()
useridcsv.close()
# print()