import pytest


class TestModels:
    """Test database models."""
    
    def test_category_creation(self, app, sample_data):
        """Test creating a category."""
        from app.models import Category
        with app.app_context():
            category = Category.query.get(sample_data['category_id'])
            assert category is not None
            assert category.name == 'Test Algebra'
            assert category.slug == 'test-algebra'
            assert category.description == 'Test algebra topics'
    
    def test_category_relationships(self, app, sample_data):
        """Test category to topic relationship."""
        from app.models import Category
        with app.app_context():
            category = Category.query.get(sample_data['category_id'])
            assert len(category.topics) > 0
            assert category.topics[0].title == 'Test Quadratic Equations'
    
    def test_topic_creation(self, app, sample_data):
        """Test creating a topic."""
        from app.models import Topic
        with app.app_context():
            topic = Topic.query.get(sample_data['topic_id'])
            assert topic.title == 'Test Quadratic Equations'
            assert topic.slug == 'test-quadratic-equations'
            assert topic.difficulty == 'intermediate'
            assert topic.views == 0
    
    def test_topic_formulas_relationship(self, app, sample_data):
        """Test topic to formulas relationship."""
        from app.models import Topic
        with app.app_context():
            topic = Topic.query.get(sample_data['topic_id'])
            assert len(topic.formulas) > 0
            assert topic.formulas[0].title == 'Test Formula'
    
    def test_topic_examples_relationship(self, app, sample_data):
        """Test topic to examples relationship."""
        from app.models import Topic
        with app.app_context():
            topic = Topic.query.get(sample_data['topic_id'])
            assert len(topic.examples) > 0
            assert topic.examples[0].title == 'Test Example'
    
    def test_formula_creation(self, app, sample_data):
        """Test creating a formula."""
        from app.models import Formula
        with app.app_context():
            formula = Formula.query.get(sample_data['formula_id'])
            assert formula.title == 'Test Formula'
            assert formula.latex == 'x = \\frac{-b}{2a}'
            assert formula.description == 'Test formula description'
    
    def test_formula_belongs_to_topic(self, app, sample_data):
        """Test formula belongs to topic."""
        from app.models import Formula
        with app.app_context():
            formula = Formula.query.get(sample_data['formula_id'])
            assert formula.topic.title == 'Test Quadratic Equations'
    
    def test_example_creation(self, app, sample_data):
        """Test creating an example."""
        from app.models import Example
        with app.app_context():
            example = Example.query.get(sample_data['example_id'])
            assert example.title == 'Test Example'
            assert example.problem == 'Solve x²'
            assert example.solution == 'x = 0'
    
    def test_example_belongs_to_topic(self, app, sample_data):
        """Test example belongs to topic."""
        from app.models import Example
        with app.app_context():
            example = Example.query.get(sample_data['example_id'])
            assert example.topic.title == 'Test Quadratic Equations'
    
    def test_topic_timestamps(self, app):
        """Test topic timestamps are set."""
        from app.models import Topic, Category
        with app.app_context():
            category = Category(name='Test', slug='test')
            db.session.add(category)
            db.session.commit()
            
            topic = Topic(
                title='Test Topic',
                slug='test-topic',
                category_id=category.id,
                content='Test'
            )
            db.session.add(topic)
            db.session.commit()
            
            assert topic.created_at is not None
            assert topic.updated_at is not None
    
    def test_category_unique_slug(self, app):
        """Test category slug must be unique."""
        from app.models import Category
        from sqlalchemy.exc import IntegrityError
        with app.app_context():
            category1 = Category(name='Test1', slug='test-slug')
            db.session.add(category1)
            db.session.commit()
            
            category2 = Category(name='Test2', slug='test-slug')
            db.session.add(category2)
            
            with pytest.raises(IntegrityError):
                db.session.commit()
    
    def test_topic_unique_slug(self, app):
        """Test topic slug must be unique."""
        from app.models import Topic, Category
        from sqlalchemy.exc import IntegrityError
        with app.app_context():
            category = Category(name='Test', slug='test')
            db.session.add(category)
            db.session.commit()
            
            topic1 = Topic(
                title='Test1',
                slug='test-slug',
                category_id=category.id,
                content='Test'
            )
            db.session.add(topic1)
            db.session.commit()
            
            topic2 = Topic(
                title='Test2',
                slug='test-slug',
                category_id=category.id,
                content='Test'
            )
            db.session.add(topic2)
            
            with pytest.raises(IntegrityError):
                db.session.commit()


class TestDatabaseOperations:
    """Test database operations."""
    
    def test_create_multiple_topics(self, app):
        """Test creating multiple topics."""
        from app.models import Category, Topic
        with app.app_context():
            category = Category(name='Test', slug='test')
            db.session.add(category)
            db.session.commit()
            
            for i in range(5):
                topic = Topic(
                    title=f'Topic {i}',
                    slug=f'topic-{i}',
                    category_id=category.id,
                    content='Test'
                )
                db.session.add(topic)
            db.session.commit()
            
            topics = Topic.query.filter_by(category_id=category.id).all()
            assert len(topics) == 5
    
    def test_delete_cascade(self, app, sample_data):
        """Test deleting category cascades to topics."""
        from app.models import Category, Topic
        with app.app_context():
            category_id = sample_data['category_id']
            
            # Delete category
            category = Category.query.get(category_id)
            db.session.delete(category)
            db.session.commit()
            
            # Check topics are deleted
            topics = Topic.query.filter_by(category_id=category_id).all()
            assert len(topics) == 0


# Import db for use in tests
from app import db
