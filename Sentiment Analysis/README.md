# Password strength checker

**Methodology:**
1. Import packages and dataset
2. Convert dataset into np array
3. Tokenize dataset using Tfidfvectorizer 
4. Train test splitting
5. Model building (xgboost classifier is used as it gave very good accuracy over logistic regressor)
6. Save model as a pikle file to be used by the flask app for predicting password strength
7. Creating flask app where user can enter password and get the password's strength

**Demo**

<img src="https://github.com/Yash4900/Python-projects/blob/master/Password%20strength%20checker/demo/demo.gif?raw=true" />
