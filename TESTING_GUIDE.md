# Testing Guide for Mathmerise

This guide covers how to test the Mathmerise web application comprehensively.

## 🧪 Testing Approach

The Mathmerise project includes three types of tests:

1. **Automated Unit Tests** - Test individual components
2. **Integration Tests** - Test complete workflows
3. **Manual Testing** - Browser-based testing

---

## 🚀 Setup Testing Environment

### 1. Install Testing Dependencies

```bash
pip install pytest pytest-cov pytest-flask
pip freeze > requirements.txt
```

### 2. Project Structure for Testing

```
mathmerise/
├── tests/
│   ├── conftest.py           # Fixtures and configuration
│   ├── test_routes.py        # Route/endpoint tests
│   ├── test_models.py        # Database model tests
│   └── test_integration.py   # Integration/workflow tests
├── run.py
└── app/
```

---

## 🧬 Automated Testing

### Running All Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=app --cov-report=html
```

### Running Specific Test Files

```bash
# Test routes only
pytest tests/test_routes.py -v

# Test models only
pytest tests/test_models.py -v

# Test integration only
pytest tests/test_integration.py -v
```

### Running Specific Tests

```bash
# Run single test
pytest tests/test_routes.py::TestMainRoutes::test_index_page -v

# Run tests matching pattern
pytest tests/ -k "search" -v

# Run tests for admin routes
pytest tests/ -k "admin" -v
```

### Test Coverage

```bash
# Generate coverage report
pytest tests/ --cov=app --cov-report=html

# View coverage in browser
open htmlcov/index.html  # macOS
# or
xdg-open htmlcov/index.html  # Linux
# or
start htmlcov/index.html  # Windows
```

---

## 📋 Test Categories

### 1. Route Tests (test_routes.py)

Tests HTTP endpoints and responses.

**Main Routes:**
- ✅ Home page (`GET /`)
- ✅ About page (`GET /about`)
- ✅ Contact page (`GET /contact`)
- ✅ Search (`GET /search?q=query`)

**Topic Routes:**
- ✅ All topics (`GET /topics/`)
- ✅ Category view (`GET /topics/category/<slug>`)
- ✅ Topic detail (`GET /topics/<slug>`)
- ✅ 404 handling

**Admin Routes:**
- ✅ Dashboard (`GET /admin/`)
- ✅ Manage categories (`GET /admin/categories`)
- ✅ Add category (`POST /admin/categories/add`)
- ✅ Manage topics (`GET /admin/topics`)
- ✅ Add topic (`POST /admin/topics/add`)

### 2. Model Tests (test_models.py)

Tests database models and relationships.

**Category Model:**
- ✅ Category creation
- ✅ Category relationships
- ✅ Unique slug constraint

**Topic Model:**
- ✅ Topic creation
- ✅ Topic timestamps
- ✅ Formula relationships
- ✅ Example relationships
- ✅ Unique slug constraint

**Formula Model:**
- ✅ Formula creation
- ✅ Topic relationship
- ✅ LaTeX content

**Example Model:**
- ✅ Example creation
- ✅ Topic relationship

### 3. Integration Tests (test_integration.py)

Tests complete user workflows.

**User Journeys:**
- ✅ Browse topics workflow
- ✅ Search workflow
- ✅ Category browsing
- ✅ Admin content creation

**Data Persistence:**
- ✅ View count persistence
- ✅ Data persistence after additions

**Error Handling:**
- ✅ 404 pages
- ✅ Empty search results
- ✅ Invalid inputs

---

## 🧪 Manual Testing Checklist

### 1. Setup & Launch

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Initialize database
python init_db.py

# Step 3: Start server
python run.py
```

### 2. Home Page Testing

**URL:** `http://localhost:5000/`

**Check:**
- [ ] Page loads without errors
- [ ] Header with navigation visible
- [ ] Search bar works
- [ ] Featured topics displayed
- [ ] Categories grid visible
- [ ] Call-to-action button present
- [ ] Footer visible
- [ ] Mobile responsive (resize browser)

### 3. Navigation Testing

**URL:** Anywhere on site

**Check:**
- [ ] Logo navigates to home
- [ ] Navigation menu items work
- [ ] Active page highlighted (if applicable)
- [ ] Search bar functional
- [ ] Mobile menu responsive

### 4. Topics Browsing

**URL:** `http://localhost:5000/topics/`

**Check:**
- [ ] All topics display
- [ ] Topics have titles
- [ ] Topics have descriptions
- [ ] Difficulty badges visible
- [ ] View count displayed
- [ ] Can filter by category
- [ ] Click topic → detail page works

### 5. Topic Detail Page

**URL:** `http://localhost:5000/topics/quadratic-equations`

**Check:**
- [ ] Topic title displayed
- [ ] Content renders correctly
- [ ] Formulas display with MathJax
- [ ] Examples show problems and solutions
- [ ] Related topics visible
- [ ] View count increments
- [ ] Category link works
- [ ] Breadcrumbs or back link available

### 6. Category Browsing

**URL:** `http://localhost:5000/topics/category/algebra`

**Check:**
- [ ] Category name displayed
- [ ] Category description visible
- [ ] Topics in category listed
- [ ] Can navigate to individual topics
- [ ] Only topics from that category shown

### 7. Search Functionality

**Test 1: Search with results**
- **URL:** `http://localhost:5000/search?q=quadratic`
- **Check:**
  - [ ] Results displayed
  - [ ] Topic found in results
  - [ ] Can click result to view topic
  - [ ] Search term highlighted

**Test 2: Search no results**
- **URL:** `http://localhost:5000/search?q=xyzabc123`
- **Check:**
  - [ ] "No results" message shown
  - [ ] User guided to browse options

**Test 3: Empty search**
- **URL:** `http://localhost:5000/search`
- **Check:**
  - [ ] Handles gracefully
  - [ ] Shows guidance or empty state

### 8. Admin Dashboard

**URL:** `http://localhost:5000/admin/`

**Check:**
- [ ] Dashboard loads
- [ ] Statistics displayed
  - [ ] Total Topics count
  - [ ] Categories count
  - [ ] Formulas count
  - [ ] Examples count
- [ ] Navigation to management pages

### 9. Admin: Manage Categories

**URL:** `http://localhost:5000/admin/categories`

**Check:**
- [ ] All categories listed in table
- [ ] Edit buttons visible
- [ ] Delete buttons visible
- [ ] "Add Category" button present
- [ ] Category details shown (name, slug)

### 10. Admin: Add Category

**URL:** `http://localhost:5000/admin/categories/add`

**Test: Add new category**
- **Fill form with:**
  ```
  Name: My Category
  Slug: my-category
  Description: Test description
  Icon: 📚
  ```
- **Check:**
  - [ ] Form validates
  - [ ] Redirects to categories list
  - [ ] New category appears in list
  - [ ] Can view it from main site

### 11. Admin: Manage Topics

**URL:** `http://localhost:5000/admin/topics`

**Check:**
- [ ] All topics listed in table
- [ ] Topic details shown (title, category, difficulty)
- [ ] Edit buttons present
- [ ] Delete buttons present
- [ ] View links work
- [ ] "Add Topic" button present

### 12. Admin: Add Topic

**URL:** `http://localhost:5000/admin/topics/add`

**Test: Add new topic**
- **Fill form with:**
  ```
  Title: Test Matrices
  Slug: test-matrices
  Category: Algebra
  Description: Learning about matrices
  Content: <h3>Introduction</h3><p>Matrices are...</p>
  Difficulty: Intermediate
  ```
- **Check:**
  - [ ] Form validates
  - [ ] Required fields enforced
  - [ ] Redirects to topics list
  - [ ] New topic appears in list
  - [ ] Can view it from main site
  - [ ] LaTeX formulas (if included) render

### 13. About Page

**URL:** `http://localhost:5000/about`

**Check:**
- [ ] Page loads
- [ ] Content displays
- [ ] Formatting correct
- [ ] Links work

### 14. Contact Page

**URL:** `http://localhost:5000/contact`

**Test 1: View form**
- [ ] Form loads
- [ ] Fields visible (name, email, subject, message)
- [ ] Submit button present

**Test 2: Submit form**
- **Fill with:**
  ```
  Name: Test User
  Email: test@example.com
  Subject: Test message
  Message: This is a test message
  ```
- **Check:**
  - [ ] Form submits
  - [ ] Validates required fields
  - [ ] Shows success message (or redirects)

### 15. Responsive Design Testing

**Desktop (1920x1080):**
- [ ] All elements visible
- [ ] No horizontal scrolling
- [ ] Navigation bar proper

**Tablet (768x1024):**
- [ ] Touch-friendly buttons
- [ ] Readable text
- [ ] Responsive layout works

**Mobile (375x667):**
- [ ] Mobile menu functional
- [ ] Stacked layout
- [ ] Readable without zooming
- [ ] Touch targets large enough

### 16. Database Testing

**Initialize and verify:**

```bash
# Run database initialization
python init_db.py

# Check database created
ls -la mathmerise.db

# Verify sample data
python
>>> from app import db, create_app
>>> from app.models import Category, Topic
>>> app = create_app()
>>> with app.app_context():
...     categories = Category.query.all()
...     print(f"Categories: {len(categories)}")
...     topics = Topic.query.all()
...     print(f"Topics: {len(topics)}")
```

---

## 🐛 Performance Testing

### Load Test with Apache Bench

```bash
# Install ab
sudo apt-get install apache2-utils

# Test home page (100 requests, 10 concurrent)
ab -n 100 -c 10 http://localhost:5000/

# Test topic page
ab -n 100 -c 10 http://localhost:5000/topics/quadratic-equations

# View results
ab -n 1000 -c 50 -g results.tsv http://localhost:5000/
```

### Browser DevTools Testing

1. **Open DevTools** (F12)
2. **Network Tab:**
   - [ ] All resources load
   - [ ] No 404 errors
   - [ ] CSS/JS load in reasonable time
   
3. **Console Tab:**
   - [ ] No JavaScript errors
   - [ ] No warnings
   
4. **Performance Tab:**
   - [ ] Page Load Time < 3s
   - [ ] Render Time < 1s

---

## 📝 Test Report Template

```
Mathmerise Testing Report
Date: [DATE]
Tester: [NAME]
Version: 1.0

AUTOMATED TESTS
═══════════════════════════════
Tests Run: __
Tests Passed: __
Tests Failed: __
Coverage: __%

Test Results:
- test_routes.py: PASS/FAIL
- test_models.py: PASS/FAIL
- test_integration.py: PASS/FAIL

MANUAL TESTS
═══════════════════════════════
✓ Functionality Tests: PASS/FAIL
✓ UI/UX Tests: PASS/FAIL
✓ Responsive Tests: PASS/FAIL
✓ Database Tests: PASS/FAIL
✓ Admin Tests: PASS/FAIL

ISSUES FOUND
═══════════════════════════════
[List any bugs or issues]

NOTES
═══════════════════════════════
[Additional observations]
```

---

## 🔧 Debugging Tips

### Enable Flask Debug Mode

```python
# In run.py or .env
export FLASK_DEBUG=1
python run.py
```

### Database Debugging

```python
# Interactive shell to query database
python
>>> from app import create_app, db
>>> from app.models import Topic
>>> app = create_app()
>>> with app.app_context():
...     topics = Topic.query.all()
...     for topic in topics:
...         print(f"{topic.title}: {topic.views} views")
```

### Request/Response Debugging

```python
# Test client debugging
from app import create_app
app = create_app()
client = app.test_client()

response = client.get('/topics/quadratic-equations')
print(f"Status: {response.status_code}")
print(f"Data: {response.data[:500]}")
```

---

## ✅ Testing Checklist

Before deployment, verify:

- [ ] All automated tests pass
- [ ] Coverage > 80%
- [ ] Home page loads in < 1s
- [ ] All routes accessible
- [ ] Admin functions work
- [ ] Database persists correctly
- [ ] Mobile responsive
- [ ] No console errors
- [ ] Search works correctly
- [ ] Contact form validates

---

## 📚 Additional Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Flask Testing](https://flask.palletsprojects.com/testing/)
- [SQLAlchemy Testing](https://docs.sqlalchemy.org/testing.html)
- [MathJax Documentation](https://docs.mathjax.org/)

---

**Ready to test? Start with: `pytest tests/ -v`**
