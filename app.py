import os
from flask import Flask

from Routes import Routes

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
    )

app.config['ENVIRONMENT'] = 'development'
app.config['SECRET_KEY'] = os.urandom(32)


Routes(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
