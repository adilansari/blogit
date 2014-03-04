from datetime import datetime
from flask import *
from flask_mongokit import Document, Connection, MongoKit

#application name
app = Flask(__name__)


class BlogPost(Document):
    __collection__ = 'posts'
    structure = {
        'title': basestring,
        'body': basestring,
        'author': basestring,
        'date_creation': datetime,
        'rank': int,
        'tags': [basestring],
    }

    required_fields = ['title', 'author', 'date_reation']
    default_values = {
        'rank': 0,
        'date_creation': datetime
    }
    use_dot_notation = True

db = MongoKit(app)
db.register([BlogPost])

@app.route('/')
def home():
    posts = db.BlogPost.find().sort("date_creation", -1)
    return render_template('home.html', posts=posts)
