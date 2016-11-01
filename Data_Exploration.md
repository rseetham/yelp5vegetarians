# Predicting Yelp Restaurant Review Rating
#### George Kim(A20253304), Rekha Seethamraju (A20353704)

### Description
Yelp has released information about 11,537 businesses for an [acadamic challenge](https://www.yelp.com/dataset_challenge). We extracted the reviews given to food/resyaurant type of buisnesses with atleast 1 useful vote. This gave us 810689 reviews to work with. 
##### Goal
From looking at the data, we've decided that a customer rates a restaurant based on 4 categories - Food, Service, Ambience, Deals. We are interested in predicting the rating a customer gives based on the review.  
##### Preprocessing the data :
We replaced all the text that was no alphabets with spaces and used the scikit=learn's [CountVectorizer] (http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) to generate unigrams, bigrams and trigrams of the entire corpus and counted the frequency of occurance. The top 100 phrases are attached. 
  
The data we will be using to train our algorithm is features extracted from the reviews and the corresponding rating.  
[The review dataset (X)](https://drive.google.com/file/d/0BzdYpQSHXz3ySVk2TlFoN29KOWM/view?usp=sharing)  
[The cooresponding rating (u)](https://drive.google.com/file/d/0BwcqM0nDKGDQRi1IeTUwcE15RkNlY29kaGdKNmxnSzVtSi1j/view?usp=sharing)
 
### Instructions 
Run george_kim.ipynb to process data and plot histograms  
Required files are to be placed in the folder called Data.    
george_kim.ipynb and Data are each within a folder called george_kim.  
##### Required files to be put folder called Data are:
[corpus_1vote_textEncoding_filter.csv](https://drive.google.com/file/d/0BzdYpQSHXz3ySVk2TlFoN29KOWM/view?usp=sharing) : contains the corpus
[corpus_1vote_textEncoding_filter.txt](https://drive.google.com/file/d/0BzdYpQSHXz3yUTRoUlZiSVJzZ1E/view?usp=sharing) : contains the corpus  
In the txt file, the reviews are not separated, in the csv the reviews are separated. Both are needed for the notebook to run.  
[numwordsList.csv](https://drive.google.com/file/d/0BwcqM0nDKGDQbVc5aTVFdER4TTdWN3dHQy1kYWtWOHFRTURv/view?usp=sharing) :  contains information on the length (number of alphanumeric characters split on whitespace) of each review.
[ratings.csv](https://drive.google.com/file/d/0BwcqM0nDKGDQRi1IeTUwcE15RkNlY29kaGdKNmxnSzVtSi1j/view?usp=sharing) : contains the target values.  
Expected runtime: 30-45 minutes on a quadcore i7 second gen machine.
    
[Refrence] (http://www.ics.uci.edu/~vpsaini/)
