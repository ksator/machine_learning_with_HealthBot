from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris=load_iris()
X = iris.data
Y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5)
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy_score(y_test,y_pred)
print ("Accuracy of SVC fitted with iris data set:",accuracy_score(y_test,y_pred))
