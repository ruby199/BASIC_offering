#!/opt/miniconda3/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)



# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Integer, default=0)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # def __repr__(self):
    #     return '<Task %r>' % self.id # return a string everytime you create an element (call self.id)

def from_dictionary_return_name(content):
    name_dic = {}
    # return str(name_dic[content])
 
    return name_dic[content]




@app.route('/', methods=['POST', 'GET']) # adding two methods that can accept


def index():
    if request.method == 'POST':
        # input_name = request.form['content'] # input 이름입력의 인풋이 content라는 id
        
        # new_task = Todo(content=input_name) # create new task from input
        
        # ***여기서 tesk)content을 사용해서 db에서 이름 찾기

        #now add into database
        
        try:
            # db.session.add(new_task)
            # db.session.commit() # commit to our database
            # return redirect('/') # redirect back to our index page
            input_name = request.form['content']
            NAME = from_dictionary_return_name(input_name)
            return '%s' % NAME
            
        
        except:
            return '이름을 잘못 입력했습니다. 다시 입력해주세요.' # 이름을 잘못 입력했습니다. 

        # return "Hello" # 여기서 이름입력! --> return 헌금번호!!
    else:
        # tasks = Todo.query.order_by(Todo.date_created).all()
        # tasks = Todo.query.order_by(Todo.date_created).first() # grabbing the first one in the table

        return render_template('index.html')
        # return render_template('index.html') #just showing the page


    #   try:
    #         return name_to_offering_num.from_dictionary_return_name('content')
        
    #     except:
    #         return '이름을 잘못 입력했습니다. 다시 입력해주세요.' # 이름을 잘못 입력했습니다. 


if __name__ == "__main__":
    app.run(debug=True)
