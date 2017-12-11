import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()#load the iris datasets to iris
#print iris.feature_names
#print iris.target_names
#print iris.data[0]#contains the data  of features in first row 
#print iris.target[0]#the label in first row 
#for i in range(len(iris.data)):
#	print "Example %d:label %s,features %s"% (i,iris.target[i],iris.data[i])
test_idx = [0,5,10,15,20,50,55,60,65,70,100,105,110,115,120]

#training data
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

print "Test data lable:%r"%test_target
print "Predicted results:%r"%clf.predict(test_data)
if test_target.all() == clf.predict(test_data).all():
	print "The prediction is perfect!"