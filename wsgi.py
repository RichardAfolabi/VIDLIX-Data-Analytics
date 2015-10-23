#
from flask import Blueprint
from routes import app

# main = Blueprint('main', __name__, template_folder='templates', static_folder='static')
#
# # Import blueprints
# app.register_blueprint(main)
#




# gunicorn wsgi:app -b 0.0.0.0:8000
# gunicorn --log-file=- onbytes.wsgi:application

if __name__ == '__main__':
    app.run()





