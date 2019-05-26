# Documentation structure

- [About this repository](#about-this-repository)  
- [machine learning 101](#machine-learning-101)  
- [Machine learning hello world demo with Python](#machine-learning-hello-world-demo-with-python)  
  - [Classification](#classification)  
  - [Supervised learning](#supervised-learning)  
  - [Iris flower data set](#iris-flower-data-set)  
  - [scikit-learn python library](#scikit-learn-python-library)  
  - [scikit-learn requirements](#scikit-learn-requirements)  
  - [scikit-learn installation](#scikit-learn-installation)  
  - [scikit-learn demo](#scikit-learn-demo)  
- [HealthBot](#healthbot)  
  - [Overview](#overview)  
  - [HealthBot and machine learning](#healthbot-and-machine-learning)  
- [Machine learning for anomaly detection demo (demo with the number of BGP prefixes received)](#machine-learning-for-anomaly-detection-demo-demo-with-the-number-of-bgp-prefixes-received)  
  - [Demo overview](#demo-overview)  
  - [requirements](#requirements)  
  - [lab building blocks](#lab-building-blocks)  
  - [lab topology](#lab-topology)  
  - [lab management IP addresses](#lab-management-ip-addresses)  
  - [Junos packages](#junos-packages)
  - [Junos configuration](#junos-configuration)  
  - [HealthBot configuration](#healthbot-configuration)  
  - [Update the number of BGP prefixes received](#update-the-number-of-bgp-prefixes-received)  
  
  
## About this repository 

Using HealthBot, it is easy to: 
- collect data from the network devices 
- store the data collected in a database
- use machine learning for anomaly detection or outlier detection    

In this repository, you will find: 
- The file [machine_learning_101.pdf](machine_learning_101.pdf)  
  The purpose of this document is to:  
    - help peoples with no machine learning background to better understand machine learning basics 
    - describe machine learning usage with Healthbot  
- The file [3sigma.xlsx](3sigma.xlsx)   
  It computes the three-sigma rule 
- The file [kmeans.xlsx](kmeans.xlsx)  
  It computes one iteration of k-means with k=2  
- Automation content to configure HealthBot.  
  Healthbot will: 
  - use openconfig to collect data from Junos devices 
  - store the data collected in its database
  - process the data collected and use machine learning algorithms to detect anomaly   

# Machine learning 101

The file [machine_learning_101.pdf](machine_learning_101.pdf): 
  - helps peoples with no machine learning background to better understand machine learning basics 
  - describes machine learning usage with Healthbot  
    
# Machine learning hello world demo with Python 

Please read first the file [machine_learning_101.pdf](machine_learning_101.pdf)  

## Classification 

Classification categorizes data points into the desired class.  
There is a distinct number of classes.  
Classes are sometimes called targets, labels or categories    

Takes as input a training set and output a classifier which predict the class for any new data point 

## Supervised learning  

The machine learning algorithm learns on a labeled dataset

##  Iris flower data set  

It has data to quantify the morphologic variation of Iris flowers of three related species.  
The iris dataset consists of measurements of three types of Iris flowers: Iris Setosa, Iris Versicolor, and Iris Virginica.  

The iris dataset is intended to be for a supervised machine learning task because it has labels.  
It is a classification problem: we are trying to determine the flower categories.  
This is a supervised classification problem.  

The dataset contains a set of 150 records under five attributes: petal length, petal width, sepal length, sepal width and species.  

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor).  
Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.  
Based on the combination of these four features, we can distinguish the species  

Classes: 3  
Samples per class: 50  
Samples total: 150  
Dimensionality: 4  

## scikit-learn python library  
Scikit-Learn, also known as sklearn, is Python general-purpose machine learning library  
Scikit-Learn is very versatile. 

## scikit-learn requirements 
sklearn requires python 3  

## scikit-learn installation  
```
pip3 install sklearn
```

## scikit-learn demo

### Load the iris dataset

```
>>> from sklearn.datasets import load_iris
>>> iris=load_iris()
```
it returns a kind of dictionary. 

### Examine the iris dataset

#### shape  
It has 150 rows and 4 columns
```
>>> iris.data.shape
(150, 4)
```
#### data attribute 
the data to learn
```
>>> iris["data"]
array([[5.1, 3.5, 1.4, 0.2],
       [4.9, 3. , 1.4, 0.2],
       [4.7, 3.2, 1.3, 0.2],
       [4.6, 3.1, 1.5, 0.2],
       [5. , 3.6, 1.4, 0.2],
       [5.4, 3.9, 1.7, 0.4],
       [4.6, 3.4, 1.4, 0.3],
       [5. , 3.4, 1.5, 0.2],
       [4.4, 2.9, 1.4, 0.2],
       [4.9, 3.1, 1.5, 0.1],
       [5.4, 3.7, 1.5, 0.2],
       [4.8, 3.4, 1.6, 0.2],
       [4.8, 3. , 1.4, 0.1],
       [4.3, 3. , 1.1, 0.1],
       [5.8, 4. , 1.2, 0.2],
       [5.7, 4.4, 1.5, 0.4],
       [5.4, 3.9, 1.3, 0.4],
       [5.1, 3.5, 1.4, 0.3],
       [5.7, 3.8, 1.7, 0.3],
       [5.1, 3.8, 1.5, 0.3],
       [5.4, 3.4, 1.7, 0.2],
       [5.1, 3.7, 1.5, 0.4],
       [4.6, 3.6, 1. , 0.2],
       [5.1, 3.3, 1.7, 0.5],
       [4.8, 3.4, 1.9, 0.2],
       [5. , 3. , 1.6, 0.2],
       [5. , 3.4, 1.6, 0.4],
       [5.2, 3.5, 1.5, 0.2],
       [5.2, 3.4, 1.4, 0.2],
       [4.7, 3.2, 1.6, 0.2],
       [4.8, 3.1, 1.6, 0.2],
       [5.4, 3.4, 1.5, 0.4],
       [5.2, 4.1, 1.5, 0.1],
       [5.5, 4.2, 1.4, 0.2],
       [4.9, 3.1, 1.5, 0.2],
       [5. , 3.2, 1.2, 0.2],
       [5.5, 3.5, 1.3, 0.2],
       [4.9, 3.6, 1.4, 0.1],
       [4.4, 3. , 1.3, 0.2],
       [5.1, 3.4, 1.5, 0.2],
       [5. , 3.5, 1.3, 0.3],
       [4.5, 2.3, 1.3, 0.3],
       [4.4, 3.2, 1.3, 0.2],
       [5. , 3.5, 1.6, 0.6],
       [5.1, 3.8, 1.9, 0.4],
       [4.8, 3. , 1.4, 0.3],
       [5.1, 3.8, 1.6, 0.2],
       [4.6, 3.2, 1.4, 0.2],
       [5.3, 3.7, 1.5, 0.2],
       [5. , 3.3, 1.4, 0.2],
       [7. , 3.2, 4.7, 1.4],
       [6.4, 3.2, 4.5, 1.5],
       [6.9, 3.1, 4.9, 1.5],
       [5.5, 2.3, 4. , 1.3],
       [6.5, 2.8, 4.6, 1.5],
       [5.7, 2.8, 4.5, 1.3],
       [6.3, 3.3, 4.7, 1.6],
       [4.9, 2.4, 3.3, 1. ],
       [6.6, 2.9, 4.6, 1.3],
       [5.2, 2.7, 3.9, 1.4],
       [5. , 2. , 3.5, 1. ],
       [5.9, 3. , 4.2, 1.5],
       [6. , 2.2, 4. , 1. ],
       [6.1, 2.9, 4.7, 1.4],
       [5.6, 2.9, 3.6, 1.3],
       [6.7, 3.1, 4.4, 1.4],
       [5.6, 3. , 4.5, 1.5],
       [5.8, 2.7, 4.1, 1. ],
       [6.2, 2.2, 4.5, 1.5],
       [5.6, 2.5, 3.9, 1.1],
       [5.9, 3.2, 4.8, 1.8],
       [6.1, 2.8, 4. , 1.3],
       [6.3, 2.5, 4.9, 1.5],
       [6.1, 2.8, 4.7, 1.2],
       [6.4, 2.9, 4.3, 1.3],
       [6.6, 3. , 4.4, 1.4],
       [6.8, 2.8, 4.8, 1.4],
       [6.7, 3. , 5. , 1.7],
       [6. , 2.9, 4.5, 1.5],
       [5.7, 2.6, 3.5, 1. ],
       [5.5, 2.4, 3.8, 1.1],
       [5.5, 2.4, 3.7, 1. ],
       [5.8, 2.7, 3.9, 1.2],
       [6. , 2.7, 5.1, 1.6],
       [5.4, 3. , 4.5, 1.5],
       [6. , 3.4, 4.5, 1.6],
       [6.7, 3.1, 4.7, 1.5],
       [6.3, 2.3, 4.4, 1.3],
       [5.6, 3. , 4.1, 1.3],
       [5.5, 2.5, 4. , 1.3],
       [5.5, 2.6, 4.4, 1.2],
       [6.1, 3. , 4.6, 1.4],
       [5.8, 2.6, 4. , 1.2],
       [5. , 2.3, 3.3, 1. ],
       [5.6, 2.7, 4.2, 1.3],
       [5.7, 3. , 4.2, 1.2],
       [5.7, 2.9, 4.2, 1.3],
       [6.2, 2.9, 4.3, 1.3],
       [5.1, 2.5, 3. , 1.1],
       [5.7, 2.8, 4.1, 1.3],
       [6.3, 3.3, 6. , 2.5],
       [5.8, 2.7, 5.1, 1.9],
       [7.1, 3. , 5.9, 2.1],
       [6.3, 2.9, 5.6, 1.8],
       [6.5, 3. , 5.8, 2.2],
       [7.6, 3. , 6.6, 2.1],
       [4.9, 2.5, 4.5, 1.7],
       [7.3, 2.9, 6.3, 1.8],
       [6.7, 2.5, 5.8, 1.8],
       [7.2, 3.6, 6.1, 2.5],
       [6.5, 3.2, 5.1, 2. ],
       [6.4, 2.7, 5.3, 1.9],
       [6.8, 3. , 5.5, 2.1],
       [5.7, 2.5, 5. , 2. ],
       [5.8, 2.8, 5.1, 2.4],
       [6.4, 3.2, 5.3, 2.3],
       [6.5, 3. , 5.5, 1.8],
       [7.7, 3.8, 6.7, 2.2],
       [7.7, 2.6, 6.9, 2.3],
       [6. , 2.2, 5. , 1.5],
       [6.9, 3.2, 5.7, 2.3],
       [5.6, 2.8, 4.9, 2. ],
       [7.7, 2.8, 6.7, 2. ],
       [6.3, 2.7, 4.9, 1.8],
       [6.7, 3.3, 5.7, 2.1],
       [7.2, 3.2, 6. , 1.8],
       [6.2, 2.8, 4.8, 1.8],
       [6.1, 3. , 4.9, 1.8],
       [6.4, 2.8, 5.6, 2.1],
       [7.2, 3. , 5.8, 1.6],
       [7.4, 2.8, 6.1, 1.9],
       [7.9, 3.8, 6.4, 2. ],
       [6.4, 2.8, 5.6, 2.2],
       [6.3, 2.8, 5.1, 1.5],
       [6.1, 2.6, 5.6, 1.4],
       [7.7, 3. , 6.1, 2.3],
       [6.3, 3.4, 5.6, 2.4],
       [6.4, 3.1, 5.5, 1.8],
       [6. , 3. , 4.8, 1.8],
       [6.9, 3.1, 5.4, 2.1],
       [6.7, 3.1, 5.6, 2.4],
       [6.9, 3.1, 5.1, 2.3],
       [5.8, 2.7, 5.1, 1.9],
       [6.8, 3.2, 5.9, 2.3],
       [6.7, 3.3, 5.7, 2.5],
       [6.7, 3. , 5.2, 2.3],
       [6.3, 2.5, 5. , 1.9],
       [6.5, 3. , 5.2, 2. ],
       [6.2, 3.4, 5.4, 2.3],
       [5.9, 3. , 5.1, 1.8]])
```
first raw
```
>>> iris.data[0]
array([5.1, 3.5, 1.4, 0.2])
```
last raw
```
>>> iris.data[-1]
array([5.9, 3. , 5.1, 1.8])
```
Let’s say you are interested in the samples 10, 25, and 50
```
>>> iris.data[[10, 25, 50]]
array([[5.4, 3.7, 1.5, 0.2],
       [5. , 3. , 1.6, 0.2],
       [7. , 3.2, 4.7, 1.4]])
>>> 
```
#### feature_names attribute
```
>>> iris["feature_names"]
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
```
#### target_names attribute 
the meaning of the labels 
```
>>> iris["target_names"]
array(['setosa', 'versicolor', 'virginica'], dtype='<U10')
>>> iris.target_names
array(['setosa', 'versicolor', 'virginica'], dtype='<U10')
>>> list(iris.target_names)
['setosa', 'versicolor', 'virginica']
```
#### target attribute 
the classification labels 
```
>>> iris["target"]
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
       2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
```
Let’s say you are interested in the samples 10, 25, and 50
```
>>> iris.target[[10, 25, 50]]
array([0, 0, 1])
```

### measure the performance of prediction 

To measure the performance of prediction, we will split the dataset into training and test sets.  
- The training set refers to data we will learn from.  
- The test set is the data we pretend not to know  
- We will use the test set to measure the performance of our learning   

#### split randomly the iris data set into a train and a test subset  

X has the data to learn and Y the target
```
>>> X = iris.data
>>> Y = iris.target
```
split randomly the iris data set into a train and a test subset.  
`test_size` is a float that represent the proportion of the dataset to include in the test split.  
The test size is 50% of the whole dataset. 

```
>>> from sklearn.model_selection import train_test_split
>>> X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5)
```
X_train has the data for the train split
```
>>> X_train
array([[5.4, 3.9, 1.7, 0.4],
       [6.7, 3.1, 4.7, 1.5],
       [5.5, 2.6, 4.4, 1.2],
       [5. , 3. , 1.6, 0.2],
       [5.7, 2.8, 4.1, 1.3],
       [5.7, 2.8, 4.5, 1.3],
       [4.6, 3.6, 1. , 0.2],
       [6.3, 2.5, 4.9, 1.5],
       [7.2, 3.6, 6.1, 2.5],
       [4.8, 3.4, 1.9, 0.2],
       [5.4, 3.9, 1.3, 0.4],
       [4.4, 3.2, 1.3, 0.2],
       [5.6, 2.8, 4.9, 2. ],
       [5.4, 3.4, 1.5, 0.4],
       [6.3, 2.9, 5.6, 1.8],
       [5.1, 3.3, 1.7, 0.5],
       [5.5, 2.4, 3.8, 1.1],
       [5. , 2.3, 3.3, 1. ],
       [5. , 3.3, 1.4, 0.2],
       [6.3, 2.7, 4.9, 1.8],
       [5.1, 3.5, 1.4, 0.2],
       [5. , 3.5, 1.3, 0.3],
       [4.3, 3. , 1.1, 0.1],
       [6.1, 2.9, 4.7, 1.4],
       [5.4, 3.7, 1.5, 0.2],
       [6.5, 3. , 5.2, 2. ],
       [6.4, 2.8, 5.6, 2.1],
       [7.9, 3.8, 6.4, 2. ],
       [7. , 3.2, 4.7, 1.4],
       [5.7, 3. , 4.2, 1.2],
       [4.5, 2.3, 1.3, 0.3],
       [4.9, 3.6, 1.4, 0.1],
       [4.8, 3. , 1.4, 0.1],
       [6.5, 3.2, 5.1, 2. ],
       [5. , 3.6, 1.4, 0.2],
       [6.2, 2.8, 4.8, 1.8],
       [4.9, 2.4, 3.3, 1. ],
       [6.9, 3.1, 4.9, 1.5],
       [5.4, 3.4, 1.7, 0.2],
       [4.4, 2.9, 1.4, 0.2],
       [4.8, 3. , 1.4, 0.3],
       [6.1, 2.6, 5.6, 1.4],
       [5.6, 3. , 4.5, 1.5],
       [5. , 3.4, 1.5, 0.2],
       [6. , 2.2, 5. , 1.5],
       [6.5, 3. , 5.8, 2.2],
       [6. , 2.2, 4. , 1. ],
       [4.9, 2.5, 4.5, 1.7],
       [6.3, 2.5, 5. , 1.9],
       [6. , 2.7, 5.1, 1.6],
       [6.4, 2.7, 5.3, 1.9],
       [7.2, 3.2, 6. , 1.8],
       [6.3, 3.4, 5.6, 2.4],
       [4.7, 3.2, 1.6, 0.2],
       [7.7, 2.6, 6.9, 2.3],
       [6.9, 3.2, 5.7, 2.3],
       [7.1, 3. , 5.9, 2.1],
       [6.8, 3. , 5.5, 2.1],
       [5.1, 3.7, 1.5, 0.4],
       [5.7, 2.6, 3.5, 1. ],
       [4.7, 3.2, 1.3, 0.2],
       [6.3, 3.3, 6. , 2.5],
       [6.2, 2.2, 4.5, 1.5],
       [5.7, 4.4, 1.5, 0.4],
       [5.6, 2.9, 3.6, 1.3],
       [6.3, 2.8, 5.1, 1.5],
       [4.8, 3.1, 1.6, 0.2],
       [5.2, 4.1, 1.5, 0.1],
       [4.9, 3.1, 1.5, 0.2],
       [6. , 3.4, 4.5, 1.6],
       [6.5, 2.8, 4.6, 1.5],
       [5.1, 2.5, 3. , 1.1],
       [7.7, 3.8, 6.7, 2.2],
       [6.9, 3.1, 5.4, 2.1],
       [6.3, 2.3, 4.4, 1.3]])
```
X_test has the data for the test split
```
>>> X_test
array([[6.7, 3.3, 5.7, 2.1],
       [5.5, 4.2, 1.4, 0.2],
       [6.4, 3.2, 5.3, 2.3],
       [6.4, 2.9, 4.3, 1.3],
       [6.7, 3. , 5. , 1.7],
       [5.9, 3. , 4.2, 1.5],
       [5.5, 2.4, 3.7, 1. ],
       [5.1, 3.8, 1.6, 0.2],
       [6.5, 3. , 5.5, 1.8],
       [5.1, 3.4, 1.5, 0.2],
       [5.8, 2.8, 5.1, 2.4],
       [6.9, 3.1, 5.1, 2.3],
       [6.1, 2.8, 4. , 1.3],
       [5.8, 2.7, 5.1, 1.9],
       [7.6, 3. , 6.6, 2.1],
       [6.1, 2.8, 4.7, 1.2],
       [7.7, 2.8, 6.7, 2. ],
       [4.6, 3.2, 1.4, 0.2],
       [6. , 2.9, 4.5, 1.5],
       [6.4, 3.1, 5.5, 1.8],
       [5.6, 2.7, 4.2, 1.3],
       [4.8, 3.4, 1.6, 0.2],
       [5.7, 2.9, 4.2, 1.3],
       [5. , 3.4, 1.6, 0.4],
       [6.7, 2.5, 5.8, 1.8],
       [5.3, 3.7, 1.5, 0.2],
       [7.4, 2.8, 6.1, 1.9],
       [5.8, 2.6, 4. , 1.2],
       [6.8, 2.8, 4.8, 1.4],
       [5.6, 3. , 4.1, 1.3],
       [7.2, 3. , 5.8, 1.6],
       [6.4, 2.8, 5.6, 2.2],
       [6.6, 3. , 4.4, 1.4],
       [7.7, 3. , 6.1, 2.3],
       [5.8, 4. , 1.2, 0.2],
       [5. , 2. , 3.5, 1. ],
       [7.3, 2.9, 6.3, 1.8],
       [6.7, 3.1, 4.4, 1.4],
       [5.5, 2.3, 4. , 1.3],
       [5.5, 2.5, 4. , 1.3],
       [6.3, 3.3, 4.7, 1.6],
       [5.2, 3.5, 1.5, 0.2],
       [5.1, 3.8, 1.5, 0.3],
       [5.6, 2.5, 3.9, 1.1],
       [5. , 3.2, 1.2, 0.2],
       [4.6, 3.1, 1.5, 0.2],
       [5.2, 2.7, 3.9, 1.4],
       [6.7, 3. , 5.2, 2.3],
       [6.8, 3.2, 5.9, 2.3],
       [5. , 3.5, 1.6, 0.6],
       [5.8, 2.7, 4.1, 1. ],
       [6.1, 3. , 4.9, 1.8],
       [6.4, 3.2, 4.5, 1.5],
       [6.2, 2.9, 4.3, 1.3],
       [5.1, 3.5, 1.4, 0.3],
       [6.1, 3. , 4.6, 1.4],
       [4.4, 3. , 1.3, 0.2],
       [5.4, 3. , 4.5, 1.5],
       [5.2, 3.4, 1.4, 0.2],
       [5.9, 3. , 5.1, 1.8],
       [4.6, 3.4, 1.4, 0.3],
       [5.7, 3.8, 1.7, 0.3],
       [6.7, 3.1, 5.6, 2.4],
       [5.5, 3.5, 1.3, 0.2],
       [5.8, 2.7, 5.1, 1.9],
       [4.9, 3. , 1.4, 0.2],
       [6.6, 2.9, 4.6, 1.3],
       [5.8, 2.7, 3.9, 1.2],
       [5.1, 3.8, 1.9, 0.4],
       [4.9, 3.1, 1.5, 0.1],
       [5.9, 3.2, 4.8, 1.8],
       [5.7, 2.5, 5. , 2. ],
       [6. , 3. , 4.8, 1.8],
       [6.7, 3.3, 5.7, 2.5],
       [6.2, 3.4, 5.4, 2.3]])
```
y_train has the target for the train split
```
>>> y_train
array([0, 1, 1, 0, 1, 1, 0, 1, 2, 0, 0, 0, 2, 0, 2, 0, 1, 1, 0, 2, 0, 0,
       0, 1, 0, 2, 2, 2, 1, 1, 0, 0, 0, 2, 0, 2, 1, 1, 0, 0, 0, 2, 1, 0,
       2, 2, 1, 2, 2, 1, 2, 2, 2, 0, 2, 2, 2, 2, 0, 1, 0, 2, 1, 0, 1, 2,
       0, 0, 0, 1, 1, 1, 2, 2, 1])
```
y_test has the target for the test split
```
>>> y_test
array([2, 0, 2, 1, 1, 1, 1, 0, 2, 0, 2, 2, 1, 2, 2, 1, 2, 0, 1, 2, 1, 0,
       1, 0, 2, 0, 2, 1, 1, 1, 2, 2, 1, 2, 0, 1, 2, 1, 1, 1, 1, 0, 0, 1,
       0, 0, 1, 2, 2, 0, 1, 2, 1, 1, 0, 1, 0, 1, 0, 2, 0, 0, 2, 0, 2, 0,
       1, 1, 0, 0, 1, 2, 2, 2, 2])
```

#### 

Support vector machines (SVM) is a set of supervised learning methods.  
Support vector classifier (SVC) is a python class capable of performing classification on a dataset.  

From the module svm import the class SVC
```
from sklearn.svm import SVC
```

Create an instance of a linear SVC
```
clf = SVC(kernel='linear',random_state=1)
```

Find a linear separator. A line separating classes. A line separating (classifying) Iris setosa from Iris virginica from Iris versicolor.  
There are many linear separator: It will choose the optimal one, the one that maximizes our confidence, the one that maximizes the geometrical margin, the one that maximizes the distance between itself and the closest/nearest data point point    

# HealthBot 

## Overview 
You can use HealthBot to collect data from the network devices, store the data collected in its database, process the data collected.  
Here's the HealthBot documentation https://techlibrary.juniper.net/documentation/product/en_US/contrail-healthbot 

## HealthBot and machine learning 

HealthBot supports machine learnings for anomaly detection and for outlier detection.  

HealthBot supports the following machine learning algorithms for anomaly detection:  
- Three-sigma rule  
- k-means for anomaly detection  

HealthBot supports the following machine learning algorithms for outlier detection: 
- DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- K-fold Three-sigma ("K-Fold Cross-Validation" using "Three-sigma")

Anomaly detection and outlier detection are both about detecting anomalies.  
In HealthBot terminology:  
- anomaly detection is time based.  
  It compares new data points from a device vs data points collected from the same device during a learning period.  
- outlier detection is group based.  
  It analyzes data from a device during a learning Period vs data from other devices during the same learning period

For more details, please refer to the file [machine_learning_101.pdf](machine_learning_101.pdf). 

# Machine learning for anomaly detection demo (demo with the number of BGP prefixes received)

## Demo overview 

In this demo, Healthbot will: 
- continuously monitor on Junos devices the number of bgp prefixes received (using Openconfig telemetry)
- store the data collected in its database
- process the database
  - use the `k-means for anomaly detection` algorithm and `3 sigma` rule to build two machine learning models
  - use the machine learning models built to classify the new datapoints as `normal` or `abnormal`   

## requirements

clone the repository
```
$ git clone https://github.com/ksator/machine_learning_with_HealthBot.git
$ cd machine_learning_with_HealthBot
```
Install the requirements on Ubuntu
```
$ sudo apt install python-pip
$ pip install --upgrade -r requirements.txt
```

## lab building blocks   

- Junos devices 
- One Ubuntu VM with healthbot installed  

## lab topology

Here's the lab topology I am using (spines and leaves).    
You can use less Junos devices if you want
![topology.png](resources/topology.png)  

## lab management IP addresses 

Here are the management ip addresses I am using in my scripts.  
If you are using other ip addresses, you need to update the file [inventory.yml](inventory.yml) to use your ip addresses  

You can use less Junos devices if you want

| Device        | Management IP address           |
| ------------- |:-------------:| 
| healthbot        | 100.123.35.0 |
| vMX1      | 100.123.1.0 |
| vMX2      | 100.123.1.1   |
| vMX3      | 100.123.1.2   |
| vMX4      | 100.123.1.3   |
| vMX5      | 100.123.1.4   |
| vMX6      | 100.123.1.5   |
| vMX7      | 100.123.1.6   |

## Junos packages

In order to collect data from Junos using openconfig telemetry, the devices require the Junos packages ```openconfig``` and ```network agent```

Starting with Junos OS Release 18.3R1: 
- the Junos OS image includes the ```OpenConfig``` package; therefore, you do not need anymore to install ```OpenConfig``` separately on your device.  
- the Junos OS image includes the ```Network Agent```, therefore, you do not need anymore to install the ```network agent``` separately on your device.  

If your setup is using an older Junos release, it is required to install these two packages:    
- Download these two packages from Juniper website and save them in your local directory.    
- Execute the python script [upgrade_junos.py](upgrade_junos.py) to add these two packages to the Junos devices indicated in this [inventory.yml](inventory.yml) file   

Update the devices inventory: 
```
$ vi inventory.yml
```
Run this command to execute the python script [upgrade_junos.py](upgrade_junos.py)
```
$ python ./upgrade_junos.py
```
ssh to a Junos device and verify it uses these packages:
```
jcluser@vMX1> file list

/var/home/jcluser/:
junos-openconfig-x86-32-0.0.0.10-1.tgz
network-agent-x86-32-18.2R1-S3.2-C1.tgz

```
```
jcluser@vMX1> show version | match "Junos:|openconfig|na telemetry"
Junos: 18.2R1.9
JUNOS na telemetry [18.2R1-S3.2-C1]
JUNOS Openconfig [0.0.0.10-1]
```

## Junos configuration

we will the python script [configure_junos.py](configure_junos.py) to configure the lab (IP fabric with EBGP)    

This script uses: 
- the template [junos.j2](configure_junos/junos.j2) 
- the variables [junos.yml](configure_junos/junos.yml) 

This script: 
- generates a junos configuration file for each device indicated in the [inventory.yml](inventory.yml) file
- saves the generated configuration files in the directory [configure_junos](configure_junos) 
- loads the junos configuration files on the devices  
 
Run this command to update the devices inventory file:
```
$ vi inventory.yml
```
Run this command to configure the lab:  
```
$ python configure_junos.py
configured device vMX1
configured device vMX2
configured device vMX3
configured device vMX4
configured device vMX5
configured device vMX6
configured device vMX7
```
The generated junos configuration files are saved in the directory [configure_junos](configure_junos).  
```
$ ls configure_junos
```
ssh to a junos device and check bgp sessions state. The sessions should be established.  
To audit BGP sessions using Python, run this command: 
```
$ python audit_junos.py
vMX1
bgp session with peer 192.168.1.1+179 is Established
bgp session with peer 192.168.1.3+179 is Established
bgp session with peer 192.168.1.5+179 is Established
bgp session with peer 192.168.1.7+61628 is Established
vMX2
bgp session with peer 192.168.2.1+179 is Established
bgp session with peer 192.168.2.3+179 is Established
bgp session with peer 192.168.2.5+179 is Established
bgp session with peer 192.168.2.7+179 is Established
vMX3
bgp session with peer 192.168.3.1+179 is Established
bgp session with peer 192.168.3.3+64639 is Established
bgp session with peer 192.168.3.5+179 is Established
bgp session with peer 192.168.3.7+61672 is Established
vMX4
bgp session with peer 192.168.1.0+55338 is Established
bgp session with peer 192.168.2.0+63710 is Established
bgp session with peer 192.168.3.0+55353 is Established
vMX5
bgp session with peer 192.168.1.2+57685 is Established
bgp session with peer 192.168.2.2+61875 is Established
bgp session with peer 192.168.3.2+179 is Established
vMX6
bgp session with peer 192.168.1.4+55251 is Established
bgp session with peer 192.168.2.4+58983 is Established
bgp session with peer 192.168.3.4+53866 is Established
vMX7
bgp session with peer 192.168.1.6+179 is Established
bgp session with peer 192.168.2.6+59682 is Established
bgp session with peer 192.168.3.6+179 is Established
```

## HealthBot configuration 

The HealthBot rule:  
- [check-bgp-state-using-openconfig.rule](rules/check-bgp-state-using-openconfig.rule) uses OpenConfig telemetry to monitor BGP sessions state (without machine learning)  
- [check-bgp-routes.rule](rules/check-bgp-routes.rule) uses OpenConfig telemetry to monitor the number of BGP prefixes received per peer, and uses a static threshold (provided as a variable) (without machine learning).  
- [check-bgp-routes-with-3-sigma.rule](rules/check-bgp-routes-with-3-sigma.rule) uses Openconfig telemetry to continuously monitor the number of bgp prefixes received, and uses `3 sigma` rule to classify the new datapoints as `normal` or `abnormal`  
- [check-bgp-routes-with-k-means.rule](rules/check-bgp-routes-with-k-means.rule) uses Openconfig telemetry to continuously monitor the number of bgp prefixes received and uses `k-means for anomaly detection` machine learning algorithm to classify the new datapoints as `normal` or `abnormal`  

The playbook [machine-learning-for-bgp.playbook](playbooks/machine-learning-for-bgp.playbook) monitors the number of BGP prefixes received using the rules:
- [check-bgp-state-using-openconfig](rules/check-bgp-state-using-openconfig.rule) (BGP sessions monitoring)  
- [check-bgp-routes](rules/check-bgp-routes.rule) (static threshold without machine learning)  
- [check-bgp-routes-with-3-sigma](rules/check-bgp-routes-with-3-sigma.rule) (dynamic threshold with 3 sigma)   
- [check-bgp-routes-with-k-means](rules/check-bgp-routes-with-k-means.rule) (dynamic threshold with k means)   

Run the script [configure_machine_learning.py](configure_machine_learning.py) to:   
- load to Healthbot the playbook [machine-learning-for-bgp.playbook](playbooks/machine-learning-for-bgp.playbook)
- load to Healthbot the rules 
  - [check-bgp-routes](rules/check-bgp-routes.rule) 
  - [check-bgp-routes-with-3-sigma](rules/check-bgp-routes-with-3-sigma.rule) 
  - [check-bgp-routes-with-k-means](rules/check-bgp-routes-with-k-means.rule)
  - [check-bgp-state-using-openconfig](rules/check-bgp-state-using-openconfig.rule)
- create a device-group `vmx` with devices `vMX1` to `vMX7` 
- instanciate the playbook [machine-learning-for-bgp.playbook](playbooks/machine-learning-for-bgp.playbook) against the device-group `vmx`  

```
$ python configure_machine_learning.py
loaded healthbot rule check-bgp-state-using-openconfig.rule
loaded healthbot rule check-bgp-routes.rule
loaded healthbot rule check-bgp-routes-with-k-means.rule
loaded healthbot rule check-bgp-routes-with-3-sigma.rule
loaded healthbot playbook machine-learning-for-bgp.playbook
loaded healthbot configuration for the device: vMX1
loaded healthbot configuration for the device: vMX2
loaded healthbot configuration for the device: vMX3
loaded healthbot configuration for the device: vMX4
loaded healthbot configuration for the device: vMX5
loaded healthbot configuration for the device: vMX6
loaded healthbot configuration for the device: vMX7
loaded healthbot configuration for the device group: vmx
healthbot configuration commited!
$
```

Healthbot is now continuously monitoring the number of bgp prefixes received (using Openconfig telemetry) and storing the data collected in its database.  
It is using the `k-means for anomaly detection` algorithm and `3 sigma` rule to build two machine learning models.  
Once the the machine learning models are built, it will use them to classify the new datapoints as `normal` or `abnormal`   

## Update the number of BGP prefixes received  

Healthbot is collecting on each devices the number of BGP prefixes received.   

To update the number of BGP prefixes received, you can use the python script [update_routes.py](update_routes.py).  
- This script uses the template [update_routes.j2](update_routes.j2).  
- It generates a junos configuration file every 60 seconds with 101 to 109 static routes (randomly), and loads this file to the Junos device vMX1 (using the replace option).  

This junos device (vMX1) uses BGP and advertises its static routes to its BGP peers  
So when we run the python script [update_routes.py](update_routes.py), it makes the number of BGP prefixes received on vMX1 peers changing every 60 seconds  

Run this command to execute the python script [update_routes.py]update_routes.py).  
```
$ python machine_learning/update_routes.py
```
Run these commands to verify: 
```
$ ps -ef | grep update_routes.py
$ more update_routes.conf 
$ ls update_routes.conf -l
$ date
```
Run these commands on vMX1 (ip 100.123.1.0) to verify:
```
jcluser@vMX-addr-0> show system commit
jcluser@vMX-addr-0> show system uptime
jcluser@vMX-addr-0> show configuration | compare rollback 1
jcluser@vMX-addr-0> show configuration routing-options static
jcluser@vMX-addr-0> show route advertising-protocol bgp 192.168.1.1
```
Run this command on vMX1 peer (ip 100.123.1.4 as example) to see the number of BGP prefixes received 
```
jcluser@vMX-addr-4> show bgp summary
```



