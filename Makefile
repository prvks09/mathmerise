.PHONY: install run dev prod init-db clean help

help:
	@echo "Mathmerise - Mathematics Learning Platform"
	@echo ""
	@echo "Available commands:"
	@echo "  make install      Install dependencies"
	@echo "  make init-db      Initialize database with sample data"
	@echo "  make dev          Run development server on localhost:5000"
	@echo "  make prod         Run production server with Gunicorn"
	@echo "  make clean        Remove database and __pycache__"
	@echo "  make reset        Clean database and reinitialize"
	@echo "  make help         Show this help message"

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

init-db:
	@echo "Initializing database with sample data..."
	python init_db.py
	@echo "✅ Database initialized!"

dev: install init-db
	@echo "Starting development server..."
	@echo "Access the application at http://localhost:5000"
	python run.py

prod: install
	@echo "Installing Gunicorn for production..."
	pip install gunicorn
	@echo "Starting production server on 0.0.0.0:5000"
	gunicorn -w 4 -b 0.0.0.0:5000 run:app

clean:
	@echo "Cleaning up..."
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -f mathmerise.db
	@echo "✅ Cleanup complete!"

reset: clean init-db
	@echo "✅ Database reset complete!"

.DEFAULT_GOAL := help
