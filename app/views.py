

from app import app

@app.route('/lab02')
def resume():
    return app.send_static_file('lab02_resume.html')
