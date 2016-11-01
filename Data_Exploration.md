# Predicting Yelp Restaurant Review Rating
#### George Kim(A20253304), Rekha Seethamraju (A20353704)

### Description
Yelp has released information about 11,537 businesses for an [acadamic challenge](https://www.yelp.com/dataset_challenge). We extracted the reviews given to food/resyaurant type of buisnesses with atleast 1 useful vote. This gave us 810689 reviews to work with.   
##### Preprocessing the data :
We replaced all the text that was no alphabets with spaces and used the scikit=learn's [CountVectorizer] (http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) to generate unigrams, bigrams and trigrams of the entire corpus and counted the frequency of occurance. The top 100 phrases are attached. 
  
The data we will be using to train our algorithm is features extracted from the reviews and the corresponding rating.  
[The review dataset (X)]()  
[The cooresponding rating (u)]()
##### Goal
From looking at the data, we've decided that a customer rates a restaurant based on 4 categories - Food, Service, Ambience, Deals. We are interested in predicting the rating a customer gives based on the review. 
  
    
[Refrence] (http://www.ics.uci.edu/~vpsaini/)
