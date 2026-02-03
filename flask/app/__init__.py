from flask import Flask, request, redirect
app = Flask(__name__, static_folder='static')
app.url_map.strict_slashes = False


app.jinja_options = app.jinja_options.copy()
app.jinja_options.update({
    'trim_blocks': True,
    'lstrip_blocks': True
})




app.config['DEBUG'] = True
app.config['SECRET_KEY'] = \
    '31678f0726e0a354a91f29a4d2a7cb5a71ac0b746957bb95'

app.config['JSON_AS_ASCII'] = False



@app.before_request
def remove_trailing_slash():
   # Check if the path ends with a slash but is not the root "/"
    if request.path != '/' and request.path.endswith('/'):
        return redirect(request.path[:-1], code=308)

from app import views