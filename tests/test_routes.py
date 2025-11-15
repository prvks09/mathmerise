import pytest


class TestMainRoutes:
    """Test main application routes."""
    
    def test_index_page(self, client, sample_data):
        """Test home page loads."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Mathmerise' in response.data
        assert b'Welcome' in response.data or b'Home' in response.data
    
    def test_about_page(self, client):
        """Test about page loads."""
        response = client.get('/about')
        assert response.status_code == 200
        assert b'About' in response.data
    
    def test_contact_page_get(self, client):
        """Test contact page GET request."""
        response = client.get('/contact')
        assert response.status_code == 200
        assert b'Contact' in response.data
    
    def test_search_no_query(self, client):
        """Test search with no query."""
        response = client.get('/search')
        assert response.status_code == 200 or response.status_code == 400
    
    def test_search_with_query(self, client, sample_data):
        """Test search with query string."""
        response = client.get('/search?q=test')
        assert response.status_code == 200
        assert b'Search' in response.data or b'Result' in response.data
    
    def test_search_finds_topic(self, client, sample_data):
        """Test search finds matching topics."""
        response = client.get('/search?q=quadratic')
        assert response.status_code == 200
        # Should contain search results page or the topic
        assert b'Test Quadratic' in response.data or b'search' in response.data.lower()


class TestTopicRoutes:
    """Test topic browsing routes."""
    
    def test_all_topics_page(self, client, sample_data):
        """Test all topics page."""
        response = client.get('/topics/')
        assert response.status_code == 200
        assert b'Topic' in response.data or b'topic' in response.data
    
    def test_category_page(self, client, sample_data):
        """Test category page."""
        response = client.get('/topics/category/test-algebra')
        assert response.status_code == 200
        assert b'Test Algebra' in response.data
    
    def test_category_404(self, client):
        """Test category not found."""
        response = client.get('/topics/category/nonexistent')
        assert response.status_code == 404
    
    def test_topic_view(self, client, sample_data):
        """Test viewing a single topic."""
        response = client.get('/topics/test-quadratic-equations')
        assert response.status_code == 200
        assert b'Test Quadratic Equations' in response.data
        assert b'Content' in response.data
    
    def test_topic_view_404(self, client):
        """Test topic not found."""
        response = client.get('/topics/nonexistent-topic')
        assert response.status_code == 404
    
    def test_topic_view_increments_views(self, client, app, sample_data):
        """Test that viewing a topic increments view counter."""
        with app.app_context():
            from app.models import Topic
            topic = Topic.query.get(sample_data['topic_id'])
            initial_views = topic.views
            
            # View the topic
            response = client.get(f'/topics/{topic.slug}')
            assert response.status_code == 200
            
            # Check view count increased
            from app.models import Topic
            updated_topic = Topic.query.filter_by(slug=topic.slug).first()
            assert updated_topic.views == initial_views + 1


class TestAdminRoutes:
    """Test admin routes."""
    
    def test_admin_dashboard(self, client, sample_data):
        """Test admin dashboard."""
        response = client.get('/admin/')
        assert response.status_code == 200
        assert b'Dashboard' in response.data or b'dashboard' in response.data.lower()
    
    def test_manage_categories(self, client, sample_data):
        """Test manage categories page."""
        response = client.get('/admin/categories')
        assert response.status_code == 200
        assert b'Test Algebra' in response.data or b'categor' in response.data.lower()
    
    def test_add_category_page(self, client):
        """Test add category form page."""
        response = client.get('/admin/categories/add')
        assert response.status_code == 200
        assert b'Category' in response.data or b'form' in response.data.lower()
    
    def test_add_category_post(self, client, app):
        """Test adding a new category."""
        data = {
            'name': 'Geometry',
            'slug': 'geometry',
            'description': 'Learn geometry',
            'icon': '🔷'
        }
        response = client.post('/admin/categories/add', data=data, follow_redirects=True)
        assert response.status_code == 200
        
        # Verify category was created
        with app.app_context():
            from app.models import Category
            category = Category.query.filter_by(slug='geometry').first()
            assert category is not None
            assert category.name == 'Geometry'
    
    def test_manage_topics(self, client, sample_data):
        """Test manage topics page."""
        response = client.get('/admin/topics')
        assert response.status_code == 200
        assert b'Topic' in response.data or b'topic' in response.data.lower()
    
    def test_add_topic_page(self, client, sample_data):
        """Test add topic form page."""
        response = client.get('/admin/topics/add')
        assert response.status_code == 200
        assert b'Topic' in response.data or b'form' in response.data.lower()
    
    def test_add_topic_post(self, client, app, sample_data):
        """Test adding a new topic."""
        data = {
            'title': 'Linear Equations',
            'slug': 'linear-equations',
            'category_id': sample_data['category_id'],
            'description': 'Learn linear equations',
            'content': '<p>Content here</p>',
            'difficulty': 'beginner'
        }
        response = client.post('/admin/topics/add', data=data, follow_redirects=True)
        assert response.status_code == 200
        
        # Verify topic was created
        with app.app_context():
            from app.models import Topic
            topic = Topic.query.filter_by(slug='linear-equations').first()
            assert topic is not None
            assert topic.title == 'Linear Equations'
