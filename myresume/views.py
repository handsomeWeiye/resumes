from flask import redirect,url_for,render_template,flash
from myresume.models import Comment
from myresume.forms import CommentForm
from myresume import app,db

@app.route('/',methods=['GET','POST'])
def index():
    db.create_all()
    comment_a = Comment(author='weiye',body='i love you')
    db.session.add(comment_a)
    db.session.commit()
    form = CommentForm()
    comments = Comment.query.order_by(Comment.timestamp.desc()).all()

    if form.validate_on_submit():
        author = form.author.data
        body = form.body.data
        comment_new = Comment(author=author,body=body)
        db.session.add(comment_new)
        db.session.commit()
        flash('Now everyone can see your replay')
        return redirect(url_for('index'))

    return render_template('index.html',  form=form,comments=comments)

