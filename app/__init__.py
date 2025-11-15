from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    # Prefer full DATABASE_URL if provided (useful for local testing or alternative DBs)
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        # Build the Cloud SQL / Postgres URL from components when running on Cloud Run
        db_user = os.getenv('DB_USER', 'postgres')
        db_pass = os.getenv('DB_PASSWORD')
        db_name = os.getenv('DB_NAME', 'mathmerise')
        instance_conn = os.getenv('INSTANCE_CONNECTION_NAME')
        if instance_conn and db_pass:
            # Use Unix socket path for Cloud SQL
            database_url = f"postgresql+psycopg2://{db_user}:{db_pass}@/{db_name}?host=/cloudsql/{instance_conn}"
        else:
            database_url = 'sqlite:///mathmerise.db'

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import and register blueprints
    from app.routes import topics, admin
    from app import routes
    app.register_blueprint(routes.bp)
    app.register_blueprint(topics.bp)
    app.register_blueprint(admin.bp)
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
