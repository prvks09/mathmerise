import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db
from app.models import Category, Topic, Formula, Example


@pytest.fixture
def app():
    """Create and configure a test Flask app."""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Create a test client for the Flask app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create a CLI runner for the Flask app."""
    return app.test_cli_runner()


@pytest.fixture
def sample_data(app):
    """Create sample data for testing."""
    with app.app_context():
        # Create category
        category = Category(
            name='Test Algebra',
            slug='test-algebra',
            description='Test algebra topics',
            icon='🔢'
        )
        db.session.add(category)
        db.session.commit()
        
        # Create topic
        topic = Topic(
            title='Test Quadratic Equations',
            slug='test-quadratic-equations',
            description='Testing quadratic equations',
            content='<h3>Content</h3><p>Test content</p>',
            category_id=category.id,
            difficulty='intermediate',
                views=0
        )
        db.session.add(topic)
        db.session.commit()
        
        # Create formula
        formula = Formula(
            topic_id=topic.id,
            title='Test Formula',
            latex='x = \\frac{-b}{2a}',
            description='Test formula description'
        )
        db.session.add(formula)
        db.session.commit()
        
        # Create example
        example = Example(
            topic_id=topic.id,
            title='Test Example',
            problem='Solve x²',
            solution='x = 0'
        )
        db.session.add(example)
        db.session.commit()
        
        return {
            'category_id': category.id,
            'topic_id': topic.id,
            'topic_slug': topic.slug,
            'formula_id': formula.id,
            'example_id': example.id
        }
