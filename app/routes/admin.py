from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Category, Topic, Formula, Example
from app import db

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
def dashboard():
    stats = {
        'total_topics': Topic.query.count(),
        'total_categories': Category.query.count(),
        'total_formulas': Formula.query.count(),
        'total_examples': Example.query.count(),
    }
    return render_template('admin/dashboard.html', stats=stats)

@bp.route('/categories')
def manage_categories():
    categories = Category.query.all()
    return render_template('admin/categories.html', categories=categories)

@bp.route('/categories/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        category = Category(
            name=request.form.get('name'),
            slug=request.form.get('slug'),
            description=request.form.get('description'),
            icon=request.form.get('icon')
        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('admin.manage_categories'))
    return render_template('admin/category_form.html')

@bp.route('/topics')
def manage_topics():
    topics = Topic.query.all()
    return render_template('admin/topics.html', topics=topics)

@bp.route('/topics/add', methods=['GET', 'POST'])
def add_topic():
    categories = Category.query.all()
    if request.method == 'POST':
        topic = Topic(
            title=request.form.get('title'),
            slug=request.form.get('slug'),
            description=request.form.get('description'),
            content=request.form.get('content'),
            category_id=request.form.get('category_id'),
            difficulty=request.form.get('difficulty', 'beginner')
        )
        db.session.add(topic)
        db.session.commit()
        return redirect(url_for('admin.manage_topics'))
    return render_template('admin/topic_form.html', categories=categories)
