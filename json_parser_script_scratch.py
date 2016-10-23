import json, os

cwd = os.getcwd()
json_review_list = []
with open(os.path.join(cwd,'yelp_training_set','yelp_training_set_review.json')) as f:
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
with open(os.path.join(cwd,'corpus'),'w') as f:
    for i in range(0,len(json_review_list)):
        
        text = json_review_list[i]['text']
        if text:
            f.write(text)
print(len(json_review_list))
print(json_review_list[0])
print(type(json_review_list[0]))
print(json_review_list[0].keys())
