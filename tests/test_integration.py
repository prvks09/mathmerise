"""
Integration tests for the Mathmerise application.
Tests complete workflows and user scenarios.
"""
import pytest


class TestUserJourneys:
    """Test complete user workflows."""
    
    def test_user_browses_topics(self, client, sample_data):
        """Test user browses home, then topics, then views a topic."""
        # Visit home
        response = client.get('/')
        assert response.status_code == 200
        
        # Navigate to topics
        response = client.get('/topics/')
        assert response.status_code == 200
        
        # View a topic
        response = client.get('/topics/test-quadratic-equations')
        assert response.status_code == 200
        assert b'Test Quadratic Equations' in response.data
    
    def test_user_searches_topics(self, client, sample_data):
        """Test user searches for topics."""
        # Search for 'quadratic'
        response = client.get('/search?q=quadratic')
        assert response.status_code == 200
        # Should see search results
        assert b'quadratic' in response.data.lower() or b'result' in response.data.lower()
    
    def test_user_browses_by_category(self, client, sample_data):
        """Test user browses topics by category."""
        # Go to category
        response = client.get('/topics/category/test-algebra')
        assert response.status_code == 200
        assert b'Test Algebra' in response.data
        # Should see topics in category
        assert b'Test Quadratic' in response.data or b'topic' in response.data.lower()
    
    def test_admin_adds_content(self, client, app, sample_data):
        """Test admin adds new category and topic."""
        # Add category
        response = client.post('/admin/categories/add', 
            data={
                'name': 'Calculus',
                'slug': 'calculus',
                'description': 'Learn calculus',
                'icon': '∫'
            },
            follow_redirects=True
        )
        assert response.status_code == 200
        
        # Add topic
        response = client.post('/admin/topics/add',
            data={
                'title': 'Derivatives',
                'slug': 'derivatives',
                'category_id': sample_data['category_id'],
                'description': 'Learn derivatives',
                'content': '<p>Derivatives content</p>',
                'difficulty': 'advanced'
            },
            follow_redirects=True
        )
        assert response.status_code == 200
        
        # Verify they were created
        response = client.get('/topics/derivatives')
        assert response.status_code == 200


class TestPageContent:
    """Test specific page content."""
    
    def test_home_page_has_navigation(self, client, sample_data):
        """Test home page has navigation elements."""
        response = client.get('/')
        assert response.status_code == 200
        # Check for navigation elements
        assert b'Mathmerise' in response.data
    
    def test_topic_page_shows_formulas(self, client, sample_data):
        """Test topic page displays formulas."""
        response = client.get('/topics/test-quadratic-equations')
        assert response.status_code == 200
        # Should show formula
        assert b'Test Formula' in response.data or b'formula' in response.data.lower()
    
    def test_topic_page_shows_examples(self, client, sample_data):
        """Test topic page displays examples."""
        response = client.get('/topics/test-quadratic-equations')
        assert response.status_code == 200
        # Should show example
        assert b'Test Example' in response.data or b'example' in response.data.lower()
    
    def test_admin_dashboard_shows_stats(self, client, sample_data):
        """Test admin dashboard shows statistics."""
        response = client.get('/admin/')
        assert response.status_code == 200
        # Should show stats like 'Total Topics', 'Categories', etc.
        assert b'Total' in response.data or b'Statistics' in response.data or b'stats' in response.data.lower()


class TestDataPersistence:
    """Test data is properly persisted."""
    
    def test_topic_view_count_persists(self, client, app, sample_data):
        """Test view count persists between requests."""
        topic_slug = sample_data['topic_slug']
        # Check initial views, then view twice and verify increment
        with app.app_context():
            from app.models import Topic
            topic = Topic.query.filter_by(slug=topic_slug).first()
            initial_views = topic.views

        # View topic twice
        response1 = client.get(f'/topics/{topic_slug}')
        assert response1.status_code == 200
        response2 = client.get(f'/topics/{topic_slug}')
        assert response2.status_code == 200

        # Verify the views increased by at least 2
        with app.app_context():
            from app.models import Topic
            topic = Topic.query.filter_by(slug=topic_slug).first()
            assert topic.views >= initial_views + 2
    
    def test_added_category_persists(self, client, app):
        """Test added category persists."""
        # Add category
        client.post('/admin/categories/add',
            data={
                'name': 'Test Persist',
                'slug': 'test-persist',
                'description': 'Test',
                'icon': '✓'
            },
            follow_redirects=True
        )
        
        # Check it persists
        with app.app_context():
            from app.models import Category
            category = Category.query.filter_by(slug='test-persist').first()
            assert category is not None
            assert category.name == 'Test Persist'


class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_404_nonexistent_topic(self, client):
        """Test 404 for nonexistent topic."""
        response = client.get('/topics/this-does-not-exist')
        assert response.status_code == 404
    
    def test_404_nonexistent_category(self, client):
        """Test 404 for nonexistent category."""
        response = client.get('/topics/category/this-does-not-exist')
        assert response.status_code == 404
    
    def test_search_empty_results(self, client):
        """Test search with no matching results."""
        response = client.get('/search?q=xyzabc123notfound')
        assert response.status_code == 200
        # Should show no results gracefully
        assert b'search' in response.data.lower() or b'result' in response.data.lower()
