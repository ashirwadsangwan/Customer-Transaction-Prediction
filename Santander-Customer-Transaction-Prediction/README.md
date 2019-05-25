# Customer-Transaction-Prediction

![alt text](https://storage.googleapis.com/kaggle-media/competitions/santander/atm_image.png)

Santander organized this competition at [Kaggle](kaggle.com) where more than 9k people participated and I received a rank of 953 which is in top 11%.

### Problem Statement
In this challenge, we had to identify which customers will make a specific transactions in future, irrespective of the amount of money transacted.

### Evaluation Metric
Submissions are evaluated on area under the ROC curve between the predicted probability and the observed target.

### Data Description
You are provided with an anonymised dataset containing numeric feature variables, the binary `target` column, and a string `ID_code` column.

The task is to predict the value of `target` column in the test set.

#### File descriptions
`train.csv` - the training set.
`test.csv` - the test set. The test set contains some rows which are not included in scoring.
`sample_submission.csv` - a sample submission file in the correct format.
