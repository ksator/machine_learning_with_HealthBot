# About this repository 

Using HealthBot, it is easy to collect data from the network devices, to store the data collected in a database, and to use machine learning for anomaly detection or outlier detection.   

In this repository, you will find: 
- The file [machine_learning_with_HealthBot.pdf](machine_learning_with_HealthBot.pdf). The purpose of this document is:  
    - to help peoples with no machine learning background to better understand machine learning basics. 
    - to describe machine learning usage with Healthbot  
- The file [3sigma.xlsx](3sigma.xlsx). It computes the three-sigma rule 
- The file [kmeans.xlsx](kmeans.xlsx). It computes one iteration of k-means with k=2  
- Configuration examples of HealthBot using machine learning to detect anomalies.  

# About HealthBot 

You can use HealthBot to collect data from the network devices, store the data collected in its database, process the data collected.  
Here's the HealthBot documentation https://techlibrary.juniper.net/documentation/product/en_US/contrail-healthbot 

# HealthBot and machine learning 

HealthBot supports machine learnings for anomaly detection and for outlier detection.  

HealthBot supports the following machine learning algorithms for anomaly detection:  
- Three-sigma rule  
- k-means for anomaly detection  

HealthBot supports the following machine learning algorithms for outlier detection: 
- DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- K-fold Three-sigma ("K-Fold Cross-Validation" using "Three-sigma")

Anomaly detection and outlier detection are both about detecting anomalies.  
In HealthBot terminology:  
- anomaly detection is time based. It compares new data points from a device vs data points collected from the same device during a learning period.  
- outlier detection is group based. It analyzes data from a device during a learning Period vs data from other devices during the same learning period

For more details, please refer to the file [machine_learning_with_HealthBot.pdf](machine_learning_with_HealthBot.pdf). 
