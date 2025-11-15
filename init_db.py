from app import db, create_app
from app.models import Category, Topic, Formula, Example

def init_db():
    """Initialize database with sample data."""
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create categories
        categories = [
            Category(
                name='Algebra',
                slug='algebra',
                description='Learn algebraic concepts including equations, polynomials, and functions',
                icon='🔢'
            ),
            Category(
                name='Geometry',
                slug='geometry',
                description='Explore shapes, angles, areas, and spatial relationships',
                icon='🔷'
            ),
            Category(
                name='Calculus',
                slug='calculus',
                description='Master derivatives, integrals, and limits',
                icon='∫'
            ),
            Category(
                name='Trigonometry',
                slug='trigonometry',
                description='Study angles, sine, cosine, and trigonometric identities',
                icon='⚡'
            ),
            Category(
                name='Statistics',
                slug='statistics',
                description='Learn probability, distributions, and data analysis',
                icon='📊'
            ),
            Category(
                name='Number Theory',
                slug='number-theory',
                description='Explore primes, factors, and integer properties',
                icon='🔐'
            )
        ]
        
        for category in categories:
            db.session.add(category)
        db.session.commit()
        
        # Create sample topics for Algebra
        algebra = Category.query.filter_by(slug='algebra').first()
        topic1 = Topic(
            title='Quadratic Equations',
            slug='quadratic-equations',
            category_id=algebra.id,
            description='Learn how to solve quadratic equations using various methods.',
            content='''
            <h3>What is a Quadratic Equation?</h3>
            <p>A quadratic equation is a polynomial equation of degree 2, written in the form:</p>
            <p><strong>ax² + bx + c = 0</strong></p>
            <p>where a, b, and c are coefficients and a ≠ 0.</p>
            
            <h3>Methods to Solve Quadratic Equations</h3>
            <ol>
                <li><strong>Factoring:</strong> Factor the equation and set each factor to zero</li>
                <li><strong>Quadratic Formula:</strong> x = (-b ± √(b² - 4ac)) / 2a</li>
                <li><strong>Completing the Square:</strong> Rearrange to form a perfect square</li>
                <li><strong>Graphing:</strong> Find where the parabola crosses the x-axis</li>
            </ol>
            
            <h3>Discriminant</h3>
            <p>The discriminant Δ = b² - 4ac determines the nature of roots:</p>
            <ul>
                <li>Δ > 0: Two distinct real roots</li>
                <li>Δ = 0: One repeated real root</li>
                <li>Δ < 0: Two complex conjugate roots</li>
            </ul>
            ''',
            difficulty='intermediate',
            views=0
        )
        db.session.add(topic1)
        db.session.commit()
        
        # Add formulas
        formula1 = Formula(
            topic_id=topic1.id,
            title='Quadratic Formula',
            latex='x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}',
            description='General formula for solving quadratic equations'
        )
        formula2 = Formula(
            topic_id=topic1.id,
            title='Discriminant',
            latex='\\Delta = b^2 - 4ac',
            description='Determines the nature of roots'
        )
        db.session.add(formula1)
        db.session.add(formula2)
        db.session.commit()
        
        # Add examples
        example1 = Example(
            topic_id=topic1.id,
            title='Solving x² - 5x + 6 = 0',
            problem='Solve the equation: x² - 5x + 6 = 0',
            solution='Using the quadratic formula: x² - 5x + 6 = (x - 2)(x - 3) = 0, so x = 2 or x = 3'
        )
        db.session.add(example1)
        db.session.commit()
        
        topic2 = Topic(
            title='Linear Equations',
            slug='linear-equations',
            category_id=algebra.id,
            description='Master the fundamentals of linear equations and systems.',
            content='''
            <h3>Linear Equations</h3>
            <p>A linear equation is an equation of the first degree. Standard form: ax + b = 0</p>
            <p>Solving: x = -b/a</p>
            <h3>Systems of Linear Equations</h3>
            <p>Methods to solve systems:</p>
            <ul>
                <li>Substitution Method</li>
                <li>Elimination Method</li>
                <li>Matrix Method</li>
            </ul>
            ''',
            difficulty='beginner',
            views=0
        )
        db.session.add(topic2)
        db.session.commit()
        
        # Create sample topics for Geometry
        geometry = Category.query.filter_by(slug='geometry').first()
        topic3 = Topic(
            title='Pythagorean Theorem',
            slug='pythagorean-theorem',
            category_id=geometry.id,
            description='Understanding the relationship between sides of a right triangle.',
            content='''
            <h3>Pythagorean Theorem</h3>
            <p>In a right triangle, the square of the hypotenuse equals the sum of squares of the other two sides.</p>
            <p><strong>a² + b² = c²</strong></p>
            <h3>Applications</h3>
            <ul>
                <li>Finding distances</li>
                <li>Checking if triangles are right triangles</li>
                <li>3D geometry calculations</li>
            </ul>
            ''',
            difficulty='intermediate',
            views=0
        )
        db.session.add(topic3)
        db.session.commit()
        
        # Create sample topics for Trigonometry
        trigonometry = Category.query.filter_by(slug='trigonometry').first()
        topic4 = Topic(
            title='Sine, Cosine, and Tangent',
            slug='sine-cosine-tangent',
            category_id=trigonometry.id,
            description='Fundamental trigonometric ratios and their applications.',
            content='''
            <h3>Trigonometric Ratios</h3>
            <p>In a right triangle:</p>
            <ul>
                <li>sin(θ) = opposite / hypotenuse</li>
                <li>cos(θ) = adjacent / hypotenuse</li>
                <li>tan(θ) = opposite / adjacent</li>
            </ul>
            <h3>SOHCAHTOA</h3>
            <p>A helpful mnemonic: Sine = Opposite/Hypotenuse, Cosine = Adjacent/Hypotenuse, Tangent = Opposite/Adjacent</p>
            ''',
            difficulty='intermediate',
            views=0
        )
        db.session.add(topic4)
        db.session.commit()
        
        print("✅ Database initialized with sample data!")
        print(f"✅ Created {len(categories)} categories")
        print(f"✅ Created {Topic.query.count()} topics")
        print(f"✅ Created {Formula.query.count()} formulas")
        print(f"✅ Created {Example.query.count()} examples")

if __name__ == '__main__':
    init_db()
