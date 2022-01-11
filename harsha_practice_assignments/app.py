from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String
from datetime import datetime

app = Flask(__name__) #creating app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# app.config['SQLALCHEMY_MODIFICATION_TRACK']=False#storing the database path in the URI
db = SQLAlchemy(app) #the database is being initialized from the settings from our app


class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200))
    completed = db.Column(db.String)
    date_created = db.Column(db.DateTime)

    def __repr__(self):
        return


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method == 'POST':
        id=request.form['id']
        content=request.form['content']
        completed=request.form['completed']
        user=Todo(id=id,content=content,completed=completed)
        db.session.add(user)
        db.session.commit()
        if user:
            return "yes"
        else:
            return "false"





    return render_template("signup.html")

if __name__ == "__main__":
    db.create_all()
    app.run(host='127.0.0.1', port=5004,debug=True)

