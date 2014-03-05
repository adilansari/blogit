from datetime import datetime
from flask import *
from flask_mongokit import Document, Connection, MongoKit
import random

#application name
app = Flask(__name__)


class BlogPost(Document):
    __collection__ = 'posts'
    structure = {
        'title': basestring,
        'body': basestring,
        'date_creation': datetime,
        'rank': int,
    }

    required_fields = ['title', 'date_creation']
    default_values = {
        'rank': 0,
        'date_creation': datetime.utcnow
    }
    use_dot_notation = True

db = MongoKit(app)
db.register([BlogPost])

def get_rank():
    u = int(random.random()*100000)
    return u

@app.route('/')
def home():
    posts = db.posts.find()
    return render_template('home.html', posts=posts)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        post = db.BlogPost()
        post.rank = get_rank()
        post.title = request.form['title']
        post.body = request.form['body']
        post.save()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
