from sklearn.model_selection import cross_val_score
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# load the data set
iris = datasets.load_iris()
X = iris.data
y = iris.target

# split the data set in a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# select a model, fit it
svc_clf = SVC(kernel = 'linear')
svc_clf.fit(X_train, y_train)

# use k fold cross validation to evaluate the trained model 
svc_scores = cross_val_score(svc_clf, X_train, y_train, cv=10)

# print the result 
print ("SVC 10 fold cross validation score:", svc_scores)
print ("SVC 10 fold cross validation mean:", svc_scores.mean())
print ("SVC 10 fold cross validation standart deviation:", svc_scores.std())

