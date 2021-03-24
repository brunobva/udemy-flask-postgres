from flask import Flask ,render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://usr_dev:bva@2021@bvadevpostgres/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route("/")
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route("/quotes")
def quotes():
    return render_template('quotes.html')

@app.route("/process",methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    
    return redirect(url_for('index'))

# app=Flask(__name__)
# @app.route('/',methods=['GET','POST'])
# def home():
#     if request.method=='POST':
#         # Handle POST Request here
#         return render_template('index.html')
#     return render_template('index.html')

# if __name__ == '__main__':
#     #DEBUG is SET to TRUE. CHANGE FOR PROD
#     app.run(port=5000,debug=True)