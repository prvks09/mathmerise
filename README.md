# Mathmerise - Mathematics Learning Platform

A comprehensive web-based platform for learning mathematics topics, built with Python Flask and SQLAlchemy.

## Overview

Mathmerise is a full-featured educational website dedicated to teaching mathematics concepts. It provides:

- **Organized Topics**: Mathematical content organized by categories
- **Search Functionality**: Find topics quickly with the search feature
- **Admin Panel**: Manage categories, topics, formulas, and examples
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Mathematical Content**: LaTeX support for formulas and equations

## Features

- 📚 Browse topics by category
- 🔍 Search across all mathematical content
- 📐 View detailed topic explanations with examples
- ∫ Display mathematical formulas using LaTeX
- 💾 Admin interface for content management
- 📊 View statistics on topic popularity
- 🎨 Modern, responsive user interface

## Quick Start

### Installation (5 minutes)

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

## Project Structure

```
mathmerise/
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── models.py                # Database models
│   ├── static/
│   │   ├── css/style.css        # Styles
│   │   ├── js/main.js           # JavaScript
│   │   └── images/              # Assets
│   ├── templates/
│   │   ├── base.html            # Base template
│   │   ├── index.html           # Home
│   │   ├── topics/              # Topic pages
│   │   └── admin/               # Admin pages
│   └── routes/
│       ├── __init__.py          # Main routes
│       ├── topics.py            # Topic routes
│       └── admin.py             # Admin routes
├── run.py                        # Entry point
├── init_db.py                    # Database setup
└── requirements.txt              # Dependencies
```

## Building & Running

### Development

```bash
python run.py
```

Access at `http://localhost:5000`

### Production

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## Database Models

- **Category**: Mathematical topic categories
- **Topic**: Educational content with descriptions
- **Formula**: Mathematical equations and formulas
- **Example**: Worked problems and solutions

## Routes

### Public
- `/` - Home
- `/topics/` - All topics
- `/topics/category/<slug>` - Category view
- `/topics/<slug>` - Topic view
- `/search?q=query` - Search
- `/about` - About page
- `/contact` - Contact form

### Admin
- `/admin/` - Dashboard
- `/admin/categories` - Manage categories
- `/admin/topics` - Manage topics

## Technologies

- **Backend**: Flask (Python)
- **Database**: SQLite / PostgreSQL
- **ORM**: SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Math**: MathJax for LaTeX rendering

## Configuration

Edit `.env`:

```
FLASK_ENV=development
DATABASE_URL=sqlite:///mathmerise.db
SECRET_KEY=your-secret-key
```

## Customization

### Adding Categories

1. Go to `/admin/categories/add`
2. Fill in name, slug, description, icon
3. Submit

### Adding Topics

1. Go to `/admin/topics/add`
2. Fill in title, content, category, difficulty
3. Submit

### Styling

Customize `app/static/css/style.css`:

```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #64748b;
}
```

## Sample Data

Includes pre-loaded topics:
- Quadratic Equations (Algebra)
- Linear Equations (Algebra)
- Pythagorean Theorem (Geometry)
- Trigonometric Functions (Trigonometry)

## Troubleshooting

### Reset Database
```bash
rm mathmerise.db
python init_db.py
```

### Change Port
Edit `run.py` and modify port number

### Missing Dependencies
```bash
pip install -r requirements.txt
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Future Enhancements

- User authentication
- Practice quizzes
- Progress tracking
- Discussion forums
- Video content
- Mobile app

## License

MIT License - Open source project

## Support

For issues or suggestions, please create an issue on GitHub.

---

**Made with ❤️ for mathematics learners everywhere**