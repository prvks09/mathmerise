# 🧪 Mathmerise Testing Checklist

Complete testing guide for the Mathmerise mathematics learning platform.

---

## 🚀 Quick Start Testing (5 minutes)

### Step 1: Setup
```bash
cd /workspaces/mathmerise
pip install -r requirements.txt
python init_db.py
python run.py
```

### Step 2: Open Browser
```
http://localhost:5000
```

### Step 3: Quick Tests
- [ ] Home page loads
- [ ] Can search for "algebra"
- [ ] Can browse topics
- [ ] Can view topic details
- [ ] Admin dashboard accessible at `/admin/`

---

## 📋 Manual Testing Checklist

### 1️⃣ HOME PAGE TESTS

**Test:** Open `http://localhost:5000/`

**Verify:**
- [ ] Page title shows "Mathmerise"
- [ ] Navigation bar visible (Home, Topics, About, Contact, Admin)
- [ ] Search bar present and functional
- [ ] Hero section with title and CTA button
- [ ] Categories grid displays 6 categories
- [ ] Featured topics section shows topics
- [ ] Mobile menu works (collapse on mobile)
- [ ] Footer visible with copyright

**Expected Results:**
- Page loads in < 2 seconds
- No console errors (F12 → Console)
- Responsive on mobile

---

### 2️⃣ NAVIGATION TESTS

**Test:** Click each navigation link

| Link | URL | Expected |
|------|-----|----------|
| Mathmerise Logo | / | Home page |
| Home | / | Home page |
| Topics | /topics/ | All topics page |
| About | /about | About page |
| Contact | /contact | Contact page |
| Admin | /admin/ | Admin dashboard |

**Verify:**
- [ ] All links work
- [ ] No 404 errors
- [ ] Active page highlighted (if applicable)

---

### 3️⃣ SEARCH FUNCTIONALITY

**Test 1: Search with results**
```
URL: http://localhost:5000/search?q=quadratic
```
**Verify:**
- [ ] Search page loads
- [ ] Results displayed
- [ ] "quadratic" appears in results
- [ ] Can click to view topic
- [ ] Number of results shown

**Test 2: Search no results**
```
URL: http://localhost:5000/search?q=xyzabc123
```
**Verify:**
- [ ] Page shows gracefully
- [ ] "No results" message
- [ ] Suggests browsing topics

**Test 3: Empty search**
```
URL: http://localhost:5000/search
```
**Verify:**
- [ ] Handles gracefully
- [ ] No error message
- [ ] Shows guidance

---

### 4️⃣ TOPICS BROWSING

**Test:** Visit `http://localhost:5000/topics/`

**Verify:**
- [ ] Page title shows "All Topics"
- [ ] Category filter dropdown present
- [ ] All 4+ topics listed
- [ ] Each topic card shows:
  - [ ] Title
  - [ ] Category name
  - [ ] Description
  - [ ] Difficulty badge (Beginner/Intermediate/Advanced)
  - [ ] View count with eye icon
  - [ ] "Learn More" button

**Test Filtering:**
- [ ] Select "Algebra" from filter
  - [ ] Only algebra topics shown
- [ ] Select "Geometry" from filter
  - [ ] Only geometry topics shown
- [ ] Select "All Categories"
  - [ ] All topics shown again

---

### 5️⃣ CATEGORY BROWSING

**Test:** Visit `http://localhost:5000/topics/category/algebra`

**Verify:**
- [ ] Category name displayed ("Algebra")
- [ ] Category description shown
- [ ] Topics in category listed
- [ ] Only topics from that category
- [ ] Can click each topic

**Try other categories:**
- [ ] /topics/category/geometry
- [ ] /topics/category/trigonometry
- [ ] /topics/category/calculus

---

### 6️⃣ TOPIC DETAIL PAGE

**Test:** Visit `http://localhost:5000/topics/quadratic-equations`

**Verify Header:**
- [ ] Topic title displayed
- [ ] Category link (clickable)
- [ ] Difficulty badge
- [ ] View count
- [ ] Last updated date

**Verify Content:**
- [ ] Main content renders
- [ ] Headings visible
- [ ] Text formatted correctly
- [ ] Formulas display with MathJax (if present)
  - Example: Should show math symbols, not raw LaTeX

**Verify Formulas Section:**
- [ ] "Key Formulas" heading
- [ ] Formula title shown
- [ ] Formula renders mathematically
- [ ] Description provided

**Verify Examples Section:**
- [ ] "Examples" heading
- [ ] Example title shown
- [ ] Problem statement visible
- [ ] Solution provided

**Verify Related Topics:**
- [ ] "Related Topics" section shows
- [ ] Related topics from same category
- [ ] Can click to view them

**View Counter Test:**
- [ ] Note current view count
- [ ] Refresh page (F5)
- [ ] View count incremented by 1
- [ ] Refresh again, verify increment

---

### 7️⃣ ABOUT PAGE

**Test:** Visit `http://localhost:5000/about`

**Verify:**
- [ ] Page loads
- [ ] Content displays
- [ ] Heading "About Mathmerise"
- [ ] Mission statement visible
- [ ] Features listed
- [ ] Proper formatting

---

### 8️⃣ CONTACT PAGE

**Test:** Visit `http://localhost:5000/contact`

**Verify Form Display:**
- [ ] Form loads
- [ ] Fields visible:
  - [ ] Name input
  - [ ] Email input
  - [ ] Subject input
  - [ ] Message textarea
  - [ ] Submit button

**Test Form Submission:**
1. Leave fields empty, click Submit
   - [ ] Validation error shown
2. Fill partial form, click Submit
   - [ ] Validation error for required fields
3. Fill complete form:
   ```
   Name: Test User
   Email: test@example.com
   Subject: Test Message
   Message: This is a test message
   ```
   - [ ] Submit succeeds
   - [ ] Success message shown (or redirect)

---

### 9️⃣ ADMIN DASHBOARD

**Test:** Visit `http://localhost:5000/admin/`

**Verify Dashboard:**
- [ ] Page loads
- [ ] "Admin Dashboard" title
- [ ] Statistics cards show:
  - [ ] Total Topics: X
  - [ ] Categories: X
  - [ ] Formulas: X
  - [ ] Examples: X
- [ ] Action buttons present:
  - [ ] Manage Categories
  - [ ] Manage Topics

**Test Navigation:**
- [ ] Click "Manage Categories" → `/admin/categories`
- [ ] Click "Manage Topics" → `/admin/topics`

---

### 🔟 ADMIN: MANAGE CATEGORIES

**Test:** Visit `http://localhost:5000/admin/categories`

**Verify Table:**
- [ ] Table displays all categories
- [ ] Columns: Name, Slug, Icon, Actions
- [ ] "Add New Category" button visible
- [ ] Each category has:
  - [ ] Edit button
  - [ ] Delete button

**Verify Data:**
- [ ] Shows all 6 categories:
  - [ ] Algebra (🔢)
  - [ ] Geometry (🔷)
  - [ ] Calculus (∫)
  - [ ] Trigonometry (⚡)
  - [ ] Statistics (📊)
  - [ ] Number Theory (🔐)

---

### 1️⃣1️⃣ ADMIN: ADD CATEGORY

**Test:** Click "Add New Category"

**Verify Form:**
- [ ] Form loads
- [ ] Fields:
  - [ ] Category Name (text input)
  - [ ] Slug (text input)
  - [ ] Description (textarea)
  - [ ] Icon (emoji input)
- [ ] Cancel button present

**Test Add Category:**
1. Leave fields empty, click Submit
   - [ ] Validation errors shown
2. Fill form:
   ```
   Name: Physics
   Slug: physics
   Description: Learn physics concepts
   Icon: ⚛️
   ```
   - [ ] Submit succeeds
   - [ ] Redirects to categories list
   - [ ] New category appears in table
3. Test on main site:
   - [ ] Visit `/topics/category/physics`
   - [ ] Page loads (should be empty or with note)

---

### 1️⃣2️⃣ ADMIN: MANAGE TOPICS

**Test:** Visit `/admin/topics`

**Verify Table:**
- [ ] Table displays all topics
- [ ] Columns: Title, Category, Difficulty, Views, Actions
- [ ] "Add New Topic" button visible
- [ ] Each topic has:
  - [ ] View link
  - [ ] Edit button
  - [ ] Delete button

**Verify Data:**
- [ ] Shows 4+ sample topics
- [ ] Column data correct:
  - [ ] Difficulty badges
  - [ ] View counts
  - [ ] Category names

---

### 1️⃣3️⃣ ADMIN: ADD TOPIC

**Test:** Click "Add New Topic"

**Verify Form:**
- [ ] Form loads
- [ ] Fields present:
  - [ ] Topic Title
  - [ ] Slug (auto-generated or manual)
  - [ ] Category (dropdown with all categories)
  - [ ] Description (textarea)
  - [ ] Content (large textarea or editor)
  - [ ] Difficulty (dropdown: Beginner/Intermediate/Advanced)
- [ ] Cancel button present

**Test Auto-slug Generation:**
1. Enter "Test Matrices" in Title
2. Leave Slug empty
3. Tab to next field
   - [ ] Slug auto-fills: "test-matrices"

**Test Add Topic:**
1. Fill form:
   ```
   Title: Test Linear Systems
   Slug: test-linear-systems
   Category: Algebra
   Description: Learn solving systems of equations
   Content: <h3>Introduction</h3><p>Systems...</p>
   Difficulty: Intermediate
   ```
   - [ ] Submit succeeds
   - [ ] Redirects to topics list
   - [ ] New topic appears
2. Test on main site:
   - [ ] Visit `/topics/test-linear-systems`
   - [ ] Content displays correctly
   - [ ] Can search for it
   - [ ] Listed in topics

---

### 1️⃣4️⃣ RESPONSIVE DESIGN

**Test on Different Screen Sizes:**

**Desktop (1920x1080):**
- [ ] All elements visible
- [ ] No horizontal scroll
- [ ] Proper spacing
- [ ] Navigation bar horizontal

**Tablet (768x1024):**
- [ ] Touch-friendly sizes
- [ ] Readable without zoom
- [ ] Responsive grid (2-3 columns)
- [ ] Form inputs large enough

**Mobile (375x667):**
- [ ] Mobile menu functional (hamburger)
- [ ] Single column layout
- [ ] Readable text
- [ ] No horizontal scroll
- [ ] Buttons touch-friendly
- [ ] Forms stack vertically

**Use Browser DevTools:**
```
F12 → Toggle Device Toolbar (Ctrl+Shift+M)
Test different presets: iPhone, iPad, etc.
```

---

### 1️⃣5️⃣ PERFORMANCE TESTING

**Test Page Load Times:**

```
Press F12 → Network tab
Reload page
Check:
  - Total load time < 3s
  - No failed requests (red)
  - All resources loaded
```

**Test Specific Pages:**

| Page | Expected Time |
|------|----------------|
| Home | < 1.5s |
| Topics | < 1.5s |
| Topic Detail | < 1s |
| Search | < 1s |
| Admin | < 1.5s |

**Check Console (F12 → Console):**
- [ ] No errors (red)
- [ ] No warnings (yellow)
- [ ] Clean console output

---

### 1️⃣6️⃣ BROWSER COMPATIBILITY

**Test in Different Browsers:**

| Browser | Result |
|---------|--------|
| Chrome | ✓ |
| Firefox | ✓ |
| Safari | ✓ |
| Edge | ✓ |

**For each browser verify:**
- [ ] Page loads
- [ ] Layout correct
- [ ] Styling applied
- [ ] No console errors
- [ ] Responsive works

---

### 1️⃣7️⃣ DATABASE PERSISTENCE

**Test Data Persistence:**

1. **Add data:**
   - Go to `/admin/categories/add`
   - Add new category
   - Note it appears in list

2. **Refresh page:**
   - F5 to refresh
   - [ ] New category still there

3. **Restart server:**
   - Kill server (Ctrl+C)
   - Restart: `python run.py`
   - [ ] New category still there

4. **View count increments:**
   - Visit a topic
   - Note view count
   - Refresh
   - [ ] View count incremented

---

### 1️⃣8️⃣ ERROR HANDLING

**Test 404 Pages:**

```
http://localhost:5000/topics/nonexistent
```
- [ ] Shows 404 error
- [ ] Friendly message
- [ ] Link to home or topics

**Test Invalid Input:**

1. Admin: Add category without name
   - [ ] Validation error shown
2. Admin: Add topic without content
   - [ ] Validation error shown
3. Contact: Submit with invalid email
   - [ ] Validation error shown

---

### 1️⃣9️⃣ AUTOMATED TESTS

**Run Route Tests:**
```bash
pytest tests/test_routes.py -v
```
Expected: Most tests pass ✓

**Run Integration Tests:**
```bash
pytest tests/test_integration.py -v
```
Expected: Tests pass ✓

**Run All Tests:**
```bash
pytest tests/ -v
```

**Generate Coverage Report:**
```bash
pytest tests/ --cov=app --cov-report=html
open htmlcov/index.html
```

---

## ✅ Final Verification Checklist

Before deployment, verify:

- [ ] **Functionality**
  - [ ] Home page loads
  - [ ] Search works
  - [ ] Topics accessible
  - [ ] Admin panel works
  - [ ] Contact form validates

- [ ] **Data**
  - [ ] Database persists
  - [ ] Sample data present
  - [ ] Can add new content
  - [ ] View counts increment

- [ ] **Design**
  - [ ] Responsive on mobile
  - [ ] Professional appearance
  - [ ] Navigation clear
  - [ ] Forms user-friendly

- [ ] **Performance**
  - [ ] Pages load < 2s
  - [ ] No console errors
  - [ ] Formulas render
  - [ ] Images load

- [ ] **Bugs**
  - [ ] No 404 errors
  - [ ] No crashes
  - [ ] Error messages helpful
  - [ ] Forms validate

---

## 🐛 Debugging Commands

**Check database:**
```bash
python3
>>> from app import create_app, db
>>> from app.models import Category, Topic
>>> app = create_app()
>>> with app.app_context():
...     print(f"Categories: {Category.query.count()}")
...     print(f"Topics: {Topic.query.count()}")
```

**Run in debug mode:**
```bash
export FLASK_DEBUG=1
python run.py
```

**View recent logs:**
```bash
tail -f run.log
```

---

## 📊 Test Results Template

```
TEST DATE: ________________
TESTER: ___________________
VERSION: __________________

AUTOMATED TESTS:
Route Tests: ____ PASSED / ____ FAILED
Integration Tests: ____ PASSED / ____ FAILED
Coverage: ____%

MANUAL TESTS:
Functionality: ✓ / ✗
Responsive: ✓ / ✗
Performance: ✓ / ✗
Browser Compat: ✓ / ✗
Data Persistence: ✓ / ✗

ISSUES FOUND:
1. ________________________________________
2. ________________________________________
3. ________________________________________

NOTES:
________________________________________
________________________________________
________________________________________
```

---

## 🎯 Testing Summary

**Total Manual Tests:** 19 test categories

**Estimated Time:** 30-45 minutes for full testing

**Pass Criteria:** All core functionality working, responsive design, no critical errors

---

**Ready to test? Start with the Quick Start section above!** 🚀
