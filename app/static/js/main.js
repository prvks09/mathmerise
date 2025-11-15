// Filter topics by category
function filterTopics() {
    const categoryFilter = document.getElementById('categoryFilter');
    const selectedCategory = categoryFilter.value;
    const topicCards = document.querySelectorAll('.topic-card');

    topicCards.forEach(card => {
        if (selectedCategory === '' || card.dataset.category === selectedCategory) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
}

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Generate slug from title
function generateSlug(title) {
    return title
        .toLowerCase()
        .trim()
        .replace(/[^\w\s-]/g, '')
        .replace(/[\s_-]+/g, '-')
        .replace(/^-+|-+$/g, '');
}

// Auto-generate slug when title changes
const titleInput = document.getElementById('title');
const slugInput = document.getElementById('slug');

if (titleInput && slugInput) {
    titleInput.addEventListener('blur', function() {
        if (!slugInput.value) {
            slugInput.value = generateSlug(this.value);
        }
    });
}

const nameInput = document.getElementById('name');
const slugInputCategory = document.getElementById('slug');

if (nameInput && slugInputCategory) {
    nameInput.addEventListener('blur', function() {
        if (!slugInputCategory.value) {
            slugInputCategory.value = generateSlug(this.value);
        }
    });
}
