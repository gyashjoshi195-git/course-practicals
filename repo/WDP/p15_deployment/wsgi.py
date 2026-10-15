from app import app   # WSGI entry point: gunicorn wsgi:app

if __name__ == "__main__":
    app.run()
