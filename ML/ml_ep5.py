#import random
from scipy.spatial import distance#a function that can caculate the distance between two points

def euc(a,b):
	return distance.euclidean(a,b)

class ScrappyKNN():  #defined ourself classifier class 
	def fit(self,X_train,y_train):#difined a fit() to training the classifier
		self.X_train = X_train
		self.y_train = y_train
		
	def predict(self,X_test):#does prediction
		predictions = []#define a list -- predictions 
		for row in X_test:
			#label = random.choice(self.y_train)
			label = self.closest(row)
			predictions.append(label)#add the type of the label to predictions list
		return predictions
	
	def closest(self,row):
		best_dist = euc(row,self.X_train[0])
		best_index = 0#use best_index to recrod the which number is the closest one in the X_test  
		for i in range(1,len(self.X_train)):
			dist = euc(row,self.X_train[i])
			if dist<best_dist:
				best_dist = dist
				best_index = i
		return self.y_train[best_index]# here we want to find the unmber of the label ,and  return the type of the label 
from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size = 0.5)#x represent feature datasets,y represent label datasets,test_size represent the sample's proportion


#from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN()

my_classifier.fit(X_train,y_train)

predictions = my_classifier.predict(X_test)

from sklearn.metrics import accuracy_score
print accuracy_score(y_test,predictions)