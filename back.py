from flask import Flask, request, render_template
import os
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")			#running the front end

@app.route('/result',methods = ['POST'])		# when query is submitted in front end
def result():
	data = request.form  						# data is empty
    											# need posted data here
	imd = data.to_dict(flat=False)
	print("answer=",imd['Query'][0])			#to convert the data type of the the query object generated to dict
	ans = imd['Query'][0]
	os.system("python test.py "+str(ans))
	f = open("output.txt", "r")					#read the sparql query and return it on front end
	line = f.read()
	f.close()
	return line

if __name__ == '__main__':
   app.run(debug = True)