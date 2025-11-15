# Mathmerise Architecture

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Web Browser (Client)                      │
│  ┌─────────────┬──────────────┬──────────────────────────┐   │
│  │   HTML5     │    CSS3      │     JavaScript           │   │
│  │  Templates  │   Responsive │   Interactivity          │   │
│  └─────────────┴──────────────┴──────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                           ↓ HTTP Requests
┌─────────────────────────────────────────────────────────────┐
│                  Flask Web Server                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                  Flask Routes                         │   │
│  │  ┌─────────┬─────────────┬──────────────────────┐   │   │
│  │  │ Main    │   Topics    │     Admin            │   │   │
│  │  │ Routes  │   Routes    │     Routes           │   │   │
│  │  ├─ /     ├─ /topics/   ├─ /admin/            │   │   │
│  │  ├─ /about├─ /topics/cat├─ /admin/categories │   │   │
│  │  ├─ /search   │ /topics/<slug> │ /admin/topics   │   │   │
│  │  └─────────┴─────────────┴──────────────────────┘   │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │             Jinja2 Template Engine                   │   │
│  │  Renders HTML templates with dynamic content         │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                           ↓ SQL Queries
┌─────────────────────────────────────────────────────────────┐
│                 SQLAlchemy ORM Layer                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Models:  Category  Topic  Formula  Example          │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                   SQLite Database                            │
│  ┌──────────┬────────┬─────────┬──────────┐                │
│  │ Category │ Topic  │ Formula │ Example  │                │
│  │ Tables   │ Tables │ Tables  │ Tables   │                │
│  └──────────┴────────┴─────────┴──────────┘                │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow Diagram

```
User Visit Website
    ↓
Browser Makes HTTP Request
    ↓
Flask Routes Handler
    ├─→ main.py (/, /about, /search, /contact)
    ├─→ topics.py (/topics/, /topics/category/, /topics/<slug>)
    └─→ admin.py (/admin/*, management)
    ↓
Query Database via SQLAlchemy
    ↓
Retrieve Category/Topic/Formula/Example Data
    ↓
Pass to Jinja2 Template Engine
    ↓
Render HTML with Dynamic Content
    ↓
Return HTML Response
    ↓
Browser Receives & Renders Page
    ├─→ Load CSS from static/css/
    ├─→ Load JS from static/js/
    └─→ Render MathJax for Formulas
    ↓
User Sees Mathematics Platform
```

## Module Structure

```
app/
│
├── __init__.py
│   └─→ Creates Flask app
│   └─→ Initializes SQLAlchemy
│   └─→ Registers blueprints
│
├── models.py
│   ├─→ Category Model
│   │   ├─ id, name, slug, description, icon
│   │   └─ Relationship: has many Topics
│   │
│   ├─→ Topic Model
│   │   ├─ id, title, slug, description, content
│   │   ├─ category_id, difficulty, views
│   │   ├─ created_at, updated_at
│   │   ├─ Relationship: belongs to Category
│   │   ├─ Relationship: has many Formulas
│   │   └─ Relationship: has many Examples
│   │
│   ├─→ Formula Model
│   │   ├─ id, topic_id, title, latex, description
│   │   └─ Relationship: belongs to Topic
│   │
│   └─→ Example Model
│       ├─ id, topic_id, title, problem, solution
│       └─ Relationship: belongs to Topic
│
├── routes/
│   ├── __init__.py (main.py equivalent)
│   │   ├─→ index()           GET /
│   │   ├─→ about()           GET /about
│   │   ├─→ contact()         GET/POST /contact
│   │   └─→ search()          GET /search
│   │
│   ├── topics.py
│   │   ├─→ all_topics()      GET /topics/
│   │   ├─→ category()        GET /topics/category/<slug>
│   │   └─→ view_topic()      GET /topics/<slug>
│   │
│   └── admin.py
│       ├─→ dashboard()       GET /admin/
│       ├─→ manage_categories() GET /admin/categories
│       ├─→ add_category()    GET/POST /admin/categories/add
│       ├─→ manage_topics()   GET /admin/topics
│       └─→ add_topic()       GET/POST /admin/topics/add
│
├── static/
│   ├── css/
│   │   └─→ style.css
│   │       ├─ Global styles
│   │       ├─ Navigation bar
│   │       ├─ Hero section
│   │       ├─ Cards & components
│   │       ├─ Forms
│   │       ├─ Admin styling
│   │       └─ Responsive breakpoints
│   │
│   ├── js/
│   │   └─→ main.js
│   │       ├─ filterTopics()
│   │       ├─ generateSlug()
│   │       └─ Event listeners
│   │
│   └── images/
│       └─→ [Image assets directory]
│
└── templates/
    │
    ├── base.html
    │   ├─ Navigation
    │   ├─ Flash messages
    │   ├─ Block content
    │   └─ Footer
    │
    ├── index.html
    │   ├─ Hero section
    │   ├─ Categories grid
    │   ├─ Featured topics
    │   └─ CTA section
    │
    ├── about.html
    │   ├─ About information
    │   └─ Mission & features
    │
    ├── contact.html
    │   └─ Contact form
    │
    ├── search_results.html
    │   ├─ Search query
    │   └─ Results list
    │
    ├── topics/
    │   ├── all_topics.html
    │   │   ├─ Filter dropdown
    │   │   └─ Topics grid
    │   │
    │   ├── category.html
    │   │   ├─ Category info
    │   │   └─ Topics in category
    │   │
    │   └── view.html
    │       ├─ Topic header
    │       ├─ Content section
    │       ├─ Formulas section
    │       ├─ Examples section
    │       ├─ Related topics
    │       └─ MathJax scripts
    │
    └── admin/
        ├── dashboard.html
        │   ├─ Statistics cards
        │   └─ Admin menu
        │
        ├── categories.html
        │   ├─ Categories table
        │   └─ Action buttons
        │
        ├── category_form.html
        │   └─ Add/edit form
        │
        ├── topics.html
        │   ├─ Topics table
        │   └─ Action buttons
        │
        └── topic_form.html
            └─ Add/edit form
```

## Database Relationships

```
Category (1) ←─── (Many) Topic
    ↓
Category:
  id → PK
  name → unique
  slug → unique
  
Topic (1) ←─── (Many) Formula
Topic (1) ←─── (Many) Example
    ↓
Topic:
  id → PK
  category_id → FK (Category.id)
  slug → unique
  
Formula:         Example:
  id → PK          id → PK
  topic_id → FK    topic_id → FK
  latex            problem
  
```

## Request/Response Cycle

```
┌──────────────────────────────────────────────────────────┐
│  1. Browser Request                                      │
│     GET http://localhost:5000/topics/quadratic-equations │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  2. Flask Routing                                        │
│     URL matches: /topics/<slug>                          │
│     Handler: topics.view_topic(slug)                     │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  3. Database Query                                       │
│     SELECT * FROM topic WHERE slug='quadratic-equations' │
│     SELECT * FROM formula WHERE topic_id=1              │
│     SELECT * FROM example WHERE topic_id=1              │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  4. Template Rendering                                   │
│     Render templates/topics/view.html                    │
│     Pass: topic, formulas, examples, related_topics     │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  5. Response Generation                                  │
│     ├─ Base HTML structure                              │
│     ├─ Navigation bar                                   │
│     ├─ Topic content with formulas                      │
│     ├─ Examples                                         │
│     ├─ CSS & JS includes                                │
│     └─ Footer                                           │
└──────────────────────────────────────────────────────────┘
                           ↓
┌──────────────────────────────────────────────────────────┐
│  6. Browser Rendering                                   │
│     ├─ Parse HTML                                       │
│     ├─ Load CSS → Apply styles                          │
│     ├─ Execute JS → Interactive features                │
│     ├─ Load MathJax → Render LaTeX formulas            │
│     └─ Display to user                                  │
└──────────────────────────────────────────────────────────┘
```

## Technology Stack Layers

```
┌─────────────────────────────────────────────────────────────┐
│  Presentation Layer                                         │
│  ├─ HTML5 Templates (Jinja2)                               │
│  ├─ CSS3 Responsive Styling                                │
│  ├─ JavaScript Interactivity                               │
│  └─ MathJax Formula Rendering                              │
├─────────────────────────────────────────────────────────────┤
│  Application Layer                                          │
│  ├─ Flask Web Framework                                    │
│  ├─ Flask-SQLAlchemy ORM                                   │
│  ├─ Flask-Migrate (Database Migrations)                    │
│  ├─ Route Handlers & Business Logic                        │
│  └─ Template Rendering (Jinja2)                            │
├─────────────────────────────────────────────────────────────┤
│  Persistence Layer                                          │
│  ├─ SQLAlchemy ORM Models                                  │
│  ├─ Database Connection Management                         │
│  ├─ SQL Query Builder                                      │
│  └─ Transaction Management                                 │
├─────────────────────────────────────────────────────────────┤
│  Data Layer                                                 │
│  └─ SQLite Database                                        │
│     ├─ Category Table                                      │
│     ├─ Topic Table                                         │
│     ├─ Formula Table                                       │
│     └─ Example Table                                       │
└─────────────────────────────────────────────────────────────┘
```

## File Dependency Graph

```
run.py (Entry Point)
   ↓
app/__init__.py (App Factory)
   ├─→ imports models.py
   ├─→ imports routes/__init__.py
   ├─→ imports routes/topics.py
   └─→ imports routes/admin.py

models.py (ORM Models)
   └─→ Used by all route handlers

routes/__init__.py (Main Routes)
   ├─→ uses models.py
   ├─→ renders templates/index.html
   ├─→ renders templates/about.html
   ├─→ renders templates/contact.html
   └─→ renders templates/search_results.html

routes/topics.py (Topic Routes)
   ├─→ uses models.py
   ├─→ renders templates/topics/all_topics.html
   ├─→ renders templates/topics/category.html
   └─→ renders templates/topics/view.html

routes/admin.py (Admin Routes)
   ├─→ uses models.py
   ├─→ renders templates/admin/dashboard.html
   ├─→ renders templates/admin/categories.html
   ├─→ renders templates/admin/category_form.html
   ├─→ renders templates/admin/topics.html
   └─→ renders templates/admin/topic_form.html

templates/base.html (Base Template)
   ├─→ included in all templates via extends
   └─→ uses static/css/style.css
   └─→ uses static/js/main.js

static/css/style.css
   └─→ Styles all HTML pages

static/js/main.js
   └─→ Adds interactivity to pages

init_db.py (Database Initialization)
   ├─→ imports app.__init__
   ├─→ imports models
   └─→ creates sample data
```

## Deployment Architecture

```
Production Server Setup:
├─ Web Server (Gunicorn)
│  ├─ 4 Worker Processes
│  ├─ Bind to 0.0.0.0:5000
│  └─ Manages WSGI Application
│
├─ Flask Application
│  ├─ Routes HTTP Requests
│  ├─ Processes Data
│  └─ Renders Responses
│
├─ Database
│  ├─ SQLite (or PostgreSQL)
│  ├─ Persists Data
│  └─ Indexed for Performance
│
└─ Static Files
   ├─ CSS (Minified)
   ├─ JavaScript (Minified)
   └─ Images (Optimized)
```

---

This architecture ensures:
- ✅ Clean separation of concerns
- ✅ Scalable and maintainable code
- ✅ Responsive user experience
- ✅ Efficient database operations
- ✅ Production-ready deployment
