from flask import Blueprint, render_template, request
from app.models import Category, Topic
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    categories = Category.query.all()
    featured_topics = Topic.query.order_by(Topic.views.desc()).limit(6).all()
    return render_template('index.html', categories=categories, featured_topics=featured_topics)

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form submission
        pass
    return render_template('contact.html')

@bp.route('/search')
def search():
    query = request.args.get('q', '').strip()
    results = []
    
    if query:
        results = Topic.query.filter(
            (Topic.title.ilike(f'%{query}%')) | 
            (Topic.description.ilike(f'%{query}%'))
        ).all()
    
    return render_template('search_results.html', query=query, results=results)
