from flask import Flask,render_template,request
app_lulu = Flask(__name__)

@app_lulu.route('/index_lulu',methods=['GET','POST'])
def index_lulu():
	nQuestions = 2
	if request.method == 'GET':
	 return render_template('userinfo_lulu.html', num=nQuestions)
	else:
	 return 'request.method was not a GET!'

if __name__ == '__main__':
	app_lulu.run(debug=True)