#encoding: utf-8

from flask import Flask
from exts import db
from bs4 import BeautifulSoup
import flask,re,requests
import config
from forms import RegistForm
from models import UserModel,QuestionModel,AnswerModel,MovieModel
from decorators import login_required
from sqlalchemy import or_

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    context = {
        'questions': QuestionModel.query.all()
    }
    return flask.render_template('index.html',**context)

@app.route('/question/',methods=['GET','POST'])
@login_required
def question():
    if flask.request.method == 'GET':
        return flask.render_template('question.html')
    else:
        title = flask.request.form.get('title')
        content = flask.request.form.get('content')
        question_model = QuestionModel(title=title,content=content)
        question_model.author = flask.g.user
        db.session.add(question_model)
        db.session.commit()
        return flask.redirect(flask.url_for('index'))

@app.route('/d/<id>/')
def detail(id):
    question_model = QuestionModel.query.get(id)
    return flask.render_template('detail.html',question=question_model)

@app.route('/comment/',methods=['POST'])
@login_required
def comment():
    question_id = flask.request.form.get('question_id')
    content = flask.request.form.get('content')
    answer_model = AnswerModel(content=content)
    answer_model.author = flask.g.user
    answer_model.question = QuestionModel.query.get(question_id)
    db.session.add(answer_model)
    db.session.commit()
    return flask.redirect(flask.url_for('detail',id=question_id))

@app.route('/search/')
def search():
    q = flask.request.args.get('q')
    questions = QuestionModel.query.filter(or_(QuestionModel.title.contains(q),QuestionModel.content.contains(q)))
    context = {
        'questions': questions
    }
    return flask.render_template('index.html',**context)

@app.route('/login/',methods=['GET','POST'])
def login():
    if flask.request.method == 'GET':
        return flask.render_template('login.html')
    else:
        telephone = flask.request.form.get('telephone')
        password = flask.request.form.get('password')
        user = UserModel.query.filter_by(telephone=telephone).first()
        if user and user.check_password(password):
            flask.session['id'] = user.id
            flask.g.user = user
            return flask.redirect(flask.url_for('index'))
        else:
            return u'用户名或密码错误！'

@app.route('/logout/',methods=['GET'])
def logout():
    flask.session.clear()
    return flask.redirect(flask.url_for('login'))

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if flask.request.method == 'GET':
        return flask.render_template('regist.html')
    else:
        form = RegistForm(flask.request.form)
        if form.validate():
            telephone = form.telephone.data
            username = form.username.data
            password = form.password1.data
            user = UserModel(telephone=telephone,username=username,password=password)
            db.session.add(user)
            db.session.commit()
            return flask.redirect(flask.url_for('login'))

@app.route('/movies/<page>',methods=['GET'])
def movies(page=1):
    pagination = MovieModel.query.paginate(int(page), per_page=30, error_out=False)
    movies = pagination.items
    print(pagination.pages)
    print(pagination.per_page)
    print(pagination.total)
    # movies = MovieModel.query.limit(10).all()
    return flask.render_template('movie.html', movies=movies, pagination=pagination)

@app.route('/movies/do/')
def movies_do():
    vip_movie = 'https://jx.618g.com/?url='
    href = flask.request.args.get("movie_url")

    if not href:
        return "输入有误！"
    real_url = vip_movie + href
    resp =requests.get(real_url).text

    soup = BeautifulSoup(resp, 'html.parser')
    frame = soup.find_all('iframe')[0]['src']
    print('*'*30)
    print(frame)
    print('*'*30)
    title = soup.title.text
    contents = {
        'frame': frame,
        'title': title
    }
    return flask.render_template('domovie.html', **contents)


@app.before_request
def before_request():
    id = flask.session.get('id')
    if id:
        user = UserModel.query.get(id)
        flask.g.user = user

@app.context_processor
def context_processor():
    if hasattr(flask.g,'user'):
        return {"user": flask.g.user}
    else:
        return {}

if __name__ == '__main__':
    app.run()
