from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String
from datetime import datetime

app = Flask(__name__) #creating app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test1.db'
# app.config['SQLALCHEMY_MODIFICATION_TRACK']=False#storing the database path in the URI
db = SQLAlchemy(app) #the database is being initialized from the settings from our app


class Todo_test(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content= request.form['content']
        task_id1= request.form['contentid']
        new_task=Todo_test(content=task_content,id=task_id1)

        try:

            db.session.add(new_task)
            db.session.commit()

            return redirect('/')
        except:
            return "There was an issue with your task.."

    else:
        tasks=Todo_test.query.order_by(Todo_test.date_created).all()
        return render_template('index.html',tasks=tasks)



@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete=Todo_test.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was problem in deleting..'


@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    task=Todo_test.query.get_or_404(id)

    if request.method =='POST':
        task.content=request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem in updating your task...'
    else:
        return render_template("update.html",task=task)



    # return render_template('index.html')
#
# @app.route("/signup",methods=["POST","GET"])
# def signup():
#     if request.method == 'POST':
#         id=request.form['id']
#         content=request.form['content']
#         completed=request.form['completed']
#         user=Todo(id=id,content=content,completed=completed)
#         db.session.add(user)
#         db.session.commit()
#         if user:
#             print("Successfuly registered")
#             return render_template('signup.html')
#         else:
#             return "false"

    # return render_template("signup.html")

if __name__ == "__main__":
    # db.create_all()
    app.run(host='127.0.0.1', port=5000,debug=True)

