from flask import Flask, render_template
from routes.user_bp import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)