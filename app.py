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
    name_dic = {'국다예슬': '271', '권찬희': '272', '김경민': '273', '김다빈': '274', '김동규': '275', '김동준': '276', '김사성': '277', '김서정': '278', '김성민': '279', '김소영': '280', '김소희': '281', '김수민': '282', '김수현': '283', '김아련': '284', '김예지': '285', '김예현': '286', '김왕종': '287', '김우빈': '288', '김주은': '289', '김태민': '290', '김태은': '291', '문지혜': '292', '박다영': '293', '박소은': '294', '박송은': '295', '박주영': '296', '박지예': '297', '박진석': '298', '백정민': '299', '변석현': '300', '손예지': '301', '손재훈': '302', '송하은': '303', '송형은': '304', '신예빈': '305', '신희준': '306', '안기범': '307', '안태휘': '308', '왕상은': '309', '왕희균': '310', '원루빈': '311', '유주평': '312', '윤다솜': '313', '윤수아': '314', '윤준기': '315', '윤한성': '316', '윤홍령': '317', '이경민': '318', '이경수': '319', '이다희': '320', '이수정': '321', '이원재': '322', '이종혁': '323', '이주환': '324', '이중표': '325', '이페트라': '326', '이현수': '327', '임나은': '328', '장지원': '329', '전예신': '330', '전푸른샘': '331', '전푸른솔': '332', '정예인': '333', '정은혜': '334', '정지현': '335', '조이안': '336', '조일조': '337', '진믿음': '338', '최성진': '339', '최원식': '340', '최진': '341', '피터박': '342', '한가원': '343', '한서윤': '344', '한정민': '345', '황동주': '346', '황동훈': '347', '황영석': '348'}
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