# Quick Start Guide for Mathmerise

## Installation (5 minutes)

```bash
# 1. Navigate to project directory
cd /workspaces/mathmerise

# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialize database with sample data
python init_db.py

# 4. Start the development server
python run.py
```

Visit `http://localhost:5000` in your browser.

## Key Features to Try

1. **Home Page** (`/`)
   - Browse featured topics
   - Explore categories
   - Access search

2. **Topics** (`/topics/`)
   - View all topics
   - Filter by category
   - See difficulty levels

3. **Individual Topic** (`/topics/quadratic-equations`)
   - Read detailed content
   - View formulas with LaTeX rendering
   - See worked examples

4. **Search** (`/?q=algebra`)
   - Search for topics by keyword
   - Filter results

5. **Admin** (`/admin/`)
   - View dashboard statistics
   - Manage categories
   - Add new topics

## Sample Topics Included

- Quadratic Equations (Algebra)
- Linear Equations (Algebra)
- Pythagorean Theorem (Geometry)
- Sine, Cosine, and Tangent (Trigonometry)

## Environment Variables

Edit `.env` to customize:

```
FLASK_ENV=development      # development or production
DATABASE_URL=sqlite:///mathmerise.db
SECRET_KEY=your-secret-key
```

## Common Commands

```bash
# Reset database
rm mathmerise.db && python init_db.py

# Run on different port
# Edit run.py and change port=5001

# Install additional packages
pip install package-name
pip freeze > requirements.txt
```

## File Structure

```
app/
  ├── models.py        # Database models
  ├── routes/          # URL routes
  ├── templates/       # HTML templates
  └── static/          # CSS & JavaScript

run.py               # Entry point
init_db.py          # Database setup
```

## Next Steps

1. Browse topics at `/topics/`
2. Explore admin panel at `/admin/`
3. Add your own categories and topics
4. Customize styling in `app/static/css/style.css`
5. Expand with more mathematical content

## Deployment

For production:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## Support

See full README.md for detailed documentation.
