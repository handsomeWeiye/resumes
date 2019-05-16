from flask import redirect,url_for,render_template,flash
from myresume.models import Author,Ability,Expextation,Comment
from myresume.forms import CommentForm
from myresume import app,db

@app.route('/',methods=['GET','POST'])
def index():
    def commit_my_resume_data():
        db.drop_all()
        db.create_all()

        author = Author(name='伟业',age=20,phone=18306832083,bio='永远的学习者')

        abilities = [Ability(
        name='程序语言',body='熟悉Python基础语法体系'
        ),
         Ability(
        name='框架',body='擅长Python-Flask 框架，MVC架构，包组织代码方式'
        ),
        Ability(
        name='爬虫',body='经常使用requests库，BeautifulSoup库，利用CSV，MySQL，mongoDB实现数据持久化'
        ),
        Ability(
        name='数据分析',body='利用NumPy，Pandas，Matplotlib进行数据分析，利用Wordcloud库实现数据可视化'
        ),
        Ability(
        name='机器学习',body='了解监督学习中的假设函数以及代价函数，解决线性回归问题'
        )]

        expectations = [Expextation(name='lifelong-learning',body='Nothing last but last learn'),\
                    Expextation(name='Communication',body='learn how to collaborate with others'),\
                    Expextation(name='Execution',body='Get things done')]

        db.session.add(author,abilities,expectations)
        db.session.commit()


    commit_my_resume_data()



    form = CommentForm()
    author = Author.query.all()
    abilities = Ability.auery.all()
    expectations = Expextation.query.all()
    comment = Comment.query.all()


    if form.validate_on_submit():
        author = form.author.data
        body = form.body.data
        comment_new = Comment(author=author,body=body)
        db.session.add(comment_new)
        db.session.commit
        flash('Now everyone can see your replay')
        return redirect(url_for('index'))

    return render_template('index.html', author=author, abilities=abilities, expectations=expectations, form=form,comment=comment)

