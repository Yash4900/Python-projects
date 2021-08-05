from flask import Flask, render_template, url_for, request
import dill
import numpy as np
import xgboost as xgb

app = Flask(__name__)

vectorizer = dill.load(open("vectorizer.pkl", "rb"))
classifier = dill.load(open("classifier.pkl", "rb"))

@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method=="POST":
		vectorizer = dill.load(open("vectorizer.pkl", "rb"))
		password = request.form['password']
		if(password==""):
			return render_template('index.html', password="", error="Please enter a password")
		x = np.array([password])
		x = vectorizer.transform(x)
		pred = classifier.predict(x)
		return render_template('index.html', password=pred, error="")
	else:	
		return render_template('index.html', password="", error="")


if __name__ == "__main__":
	app.run(debug=True)