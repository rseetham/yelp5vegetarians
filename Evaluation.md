# Predicting Yelp Review Rating
#### George Kim (A20253304), Rekha Seethamraju (A20353704)

### Description
Yelp has released information about 11,537 businesses for an [acadamic challenge](https://www.yelp.com/dataset_challenge). We extracted the reviews with atleast 1 useful vote. The reviews had a rating between 1-5. Our output class has values {pos, neutral, neg}. We conerted reviews rated 1,2 as neg; 3 as neutral and 4,5 as positive.

### Process followed
This gave us over 1 million reviews to work with. The entire dataset was too huge to work with (our computer would crash), so we picked a random sampling of 1/90th of the reviews and performed model selection on them project on them. We preprocessed the data and ran GridSearchCV with various parameters for various classifiers like : 
RidgeClassifier, Perceptron, PassiveAggressiveClassifier, KNeighborsClassifier, RandomForestClassifier, LogisticRegression, MultinomialNB, NearestCentroid and SGDClassifier

### Preprocessing
We tokenised each review and ran the Porter Stemmer from nltk package on each word after removing punctuation marks. Features were selected by running the TDIFVectorizer over the stemmed review. 

### Instructions 
Run Predicting Yelp Review Rating.ipynb to process data  
Required files are to be placed in the folder called Data.    
Predicting Yelp Review Rating.ipynb and Data are each within a folder called george_kim. 
##### Required files to be put folder called Data are:
[ratingInt_reviewStr.json](https://drive.google.com/file/d/0BzdYpQSHXz3ySVk2TlFoN29KOWM/view?usp=sharing) : contains the dataset


### Conclusion
SGDClassifier performed the best with the pollowing features : 
SGDClassifier(alpha=0.0001, average=False, class_weight=None, epsilon=0.1,  
       eta0=0.0, fit_intercept=True, l1_ratio=0.15,  
       learning_rate='optimal', loss='hinge', n_iter=50, n_jobs=1,  
       penalty='l2', power_t=0.5, random_state=None, shuffle=True,  
       verbose=0, warm_start=False)  
       
### Refrences 
(http://scikit-learn.org/stable/auto_examples/text/document_classification_20newsgroups.html)  
(http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)  
(http://textminingonline.com/dive-into-nltk-part-iv-stemming-and-lemmatization)  
