#!/bin/bash
# Quick Testing Script for Mathmerise
# This script provides a simple way to test the application

set -e

echo "╔════════════════════════════════════════════════════════╗"
echo "║                  MATHMERISE TESTING SUITE               ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print section headers
print_header() {
    echo -e "${BLUE}>>> $1${NC}"
}

# Function to print success
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

# Function to print error
print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Test 1: Check dependencies
print_header "Test 1: Checking Dependencies"
if python3 -c "import flask, sqlalchemy, pytest" 2>/dev/null; then
    print_success "All dependencies installed"
else
    print_error "Missing dependencies - installing..."
    pip install -q Flask Flask-SQLAlchemy pytest pytest-flask pytest-cov
    print_success "Dependencies installed"
fi

# Test 2: Initialize database
print_header "Test 2: Initializing Database"
if [ -f "mathmerise.db" ]; then
    print_success "Database already exists"
    rm -f mathmerise.db
    print_success "Database reset"
fi

python3 init_db.py > /dev/null 2>&1
if [ -f "mathmerise.db" ]; then
    print_success "Database created successfully"
else
    print_error "Failed to create database"
    exit 1
fi

# Test 3: Verify imports
print_header "Test 3: Verifying Application Imports"
python3 << 'EOF'
try:
    from app import create_app, db
    from app.models import Category, Topic, Formula, Example
    print("✓ All modules imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")
    exit(1)
EOF

# Test 4: Test database content
print_header "Test 4: Verifying Database Content"
python3 << 'EOF'
from app import create_app, db
from app.models import Category, Topic, Formula, Example

app = create_app()
with app.app_context():
    categories = Category.query.count()
    topics = Topic.query.count()
    formulas = Formula.query.count()
    examples = Example.query.count()
    
    print(f"✓ Categories: {categories}")
    print(f"✓ Topics: {topics}")
    print(f"✓ Formulas: {formulas}")
    print(f"✓ Examples: {examples}")
    
    if categories > 0 and topics > 0:
        print("✓ Sample data loaded successfully")
    else:
        print("✗ No sample data found")
        exit(1)
EOF

# Test 5: Run route tests
print_header "Test 5: Running Route Tests"
pytest tests/test_routes.py -q --tb=no 2>/dev/null
ROUTE_TESTS=$?

# Test 6: Run integration tests
print_header "Test 6: Running Integration Tests"
pytest tests/test_integration.py -q --tb=no 2>/dev/null
INTEGRATION_TESTS=$?

# Test 7: Quick functionality test
print_header "Test 7: Quick Functionality Test"
python3 << 'EOF'
from app import create_app

app = create_app()
client = app.test_client()

# Test home page
response = client.get('/')
assert response.status_code == 200, "Home page failed"
print("✓ Home page loads")

# Test topics page
response = client.get('/topics/')
assert response.status_code == 200, "Topics page failed"
print("✓ Topics page loads")

# Test search
response = client.get('/search?q=test')
assert response.status_code == 200, "Search failed"
print("✓ Search works")

# Test admin
response = client.get('/admin/')
assert response.status_code == 200, "Admin dashboard failed"
print("✓ Admin dashboard loads")

print("✓ All functionality tests passed")
EOF

# Summary
echo ""
echo "╔════════════════════════════════════════════════════════╗"
echo "║                    TEST SUMMARY                         ║"
echo "╚════════════════════════════════════════════════════════╝"
print_success "Setup and initialization complete"
print_success "Database created with sample data"
print_success "All core functionality working"
echo ""
echo "Next steps:"
echo "  1. Start the development server: python run.py"
echo "  2. Open browser: http://localhost:5000"
echo "  3. Run full tests: pytest tests/ -v"
echo ""
