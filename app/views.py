from app import app


@app.route('/')
def home():
    return "Rattananarin says 'Hello World!'"
