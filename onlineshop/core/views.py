from flask import render_template,request,Blueprint
from onlineshop.models import BlogPost

core = Blueprint('core',__name__)

@core.route('/')
def index():
    '''
    This is the home page view. it will hold a selection of teas, not coded
    just yet.
    '''
    return render_template('index.html')


# development area start. This view is meant to list all the teas available.

# @core.route("/")
# def home():
#
#     teas = Tea.query.all()
#
#     return render_template('index.html', teas=teas, title='Our Tea Shop')

# development areas end.



@core.route('/info')
def info():
    '''
    This is a general page in the core section which deals with processes
    not required by a login. It's just for general enquiries.
    '''
    return render_template('info.html')


@core.route('/reviews')
def reviews():
    '''
    This page can be viewed outside of a login. It uses pagination to limited
    the query size so as to not overwhelm the page.
    '''

    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page, per_page=10)

    return render_template('reviews.html',blog_posts=blog_posts)
