from flask import Flask
from admin_route import admin_bp

app = Flask(__name__)
app.register_blueprint(admin_bp)

@app.route("/")
def index():
    return "Welcome to API Passworld v2 🧠🔐"

if __name__ == "__main__":
    app.run(debug=True)


