#!/bin/bash
# Mathmerise Verification Script
# This script verifies that the project is properly set up

echo "🔍 Mathmerise Installation Verification"
echo "========================================"
echo ""

# Check Python
echo -n "✓ Checking Python... "
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "$PYTHON_VERSION"
else
    echo "❌ Python not found!"
    exit 1
fi

# Check pip
echo -n "✓ Checking pip... "
if command -v pip3 &> /dev/null; then
    PIP_VERSION=$(pip3 --version)
    echo "$PIP_VERSION"
else
    echo "❌ pip not found!"
    exit 1
fi

# Check directory structure
echo ""
echo "✓ Checking directory structure..."

REQUIRED_DIRS=(
    "app"
    "app/routes"
    "app/templates"
    "app/static"
    "app/static/css"
    "app/static/js"
)

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "  ✓ $dir/"
    else
        echo "  ❌ $dir/ NOT FOUND"
    fi
done

# Check required files
echo ""
echo "✓ Checking required files..."

REQUIRED_FILES=(
    "app/__init__.py"
    "app/models.py"
    "app/routes/__init__.py"
    "app/routes/topics.py"
    "app/routes/admin.py"
    "app/static/css/style.css"
    "app/static/js/main.js"
    "run.py"
    "init_db.py"
    "requirements.txt"
    ".env"
    "README.md"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✓ $file"
    else
        echo "  ❌ $file NOT FOUND"
    fi
done

# Check templates
echo ""
echo "✓ Checking templates..."

TEMPLATES=(
    "app/templates/base.html"
    "app/templates/index.html"
    "app/templates/about.html"
    "app/templates/contact.html"
    "app/templates/search_results.html"
    "app/templates/topics/all_topics.html"
    "app/templates/topics/category.html"
    "app/templates/topics/view.html"
    "app/templates/admin/dashboard.html"
    "app/templates/admin/categories.html"
    "app/templates/admin/topics.html"
)

for template in "${TEMPLATES[@]}"; do
    if [ -f "$template" ]; then
        echo "  ✓ $template"
    else
        echo "  ❌ $template NOT FOUND"
    fi
done

# Check if dependencies can be installed
echo ""
echo "✓ Checking dependencies..."

REQUIRED_PACKAGES=(
    "Flask"
    "SQLAlchemy"
    "Werkzeug"
)

for package in "${REQUIRED_PACKAGES[@]}"; do
    if python3 -c "import importlib; importlib.import_module('$package'.lower())" 2>/dev/null; then
        echo "  ✓ $package installed"
    else
        echo "  ⚠ $package not yet installed (will be installed via pip)"
    fi
done

# Count files
echo ""
echo "✓ Project Statistics:"
echo "  Python files: $(find app -name "*.py" | wc -l)"
echo "  HTML templates: $(find app/templates -name "*.html" | wc -l)"
echo "  CSS files: $(find app/static/css -name "*.css" | wc -l)"
echo "  JavaScript files: $(find app/static/js -name "*.js" | wc -l)"

# Next steps
echo ""
echo "========================================"
echo "✅ Verification Complete!"
echo ""
echo "📝 Next Steps:"
echo "  1. pip install -r requirements.txt"
echo "  2. python init_db.py"
echo "  3. python run.py"
echo "  4. Visit http://localhost:5000"
echo ""
echo "📖 Documentation:"
echo "  - README.md - Full documentation"
echo "  - QUICKSTART.md - Quick start guide"
echo "  - BUILD_SUMMARY.md - Build summary"
echo "  - ARCHITECTURE.md - Architecture overview"
echo ""
