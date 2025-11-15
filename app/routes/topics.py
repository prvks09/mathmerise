from flask import Blueprint, render_template, abort
from app.models import Category, Topic
from sqlalchemy import func

bp = Blueprint('topics', __name__, url_prefix='/topics')

@bp.route('/')
def all_topics():
    categories = Category.query.all()
    topics = Topic.query.all()
    return render_template('topics/all_topics.html', categories=categories, topics=topics)

@bp.route('/category/<slug>')
def category(slug):
    category = Category.query.filter_by(slug=slug).first_or_404()
    topics = Topic.query.filter_by(category_id=category.id).all()
    return render_template('topics/category.html', category=category, topics=topics)

@bp.route('/<slug>')
def view_topic(slug):
    topic = Topic.query.filter_by(slug=slug).first_or_404()
    topic.views += 1
    from app import db
    db.session.commit()
    
    related_topics = Topic.query.filter(
        Topic.category_id == topic.category_id,
        Topic.id != topic.id
    ).limit(4).all()
    
    return render_template('topics/view.html', topic=topic, related_topics=related_topics)
