from flask import Flask
from admin_route import admin_bp
from guess_route import guess_bp

app = Flask(__name__)

# Register routes *after* app is defined
app.register_blueprint(admin_bp)
app.register_blueprint(guess_bp)

@app.route("/")
def index():
    return "Welcome to the Passworld API 🧠🔐"

if __name__ == "__main__":
    app.run(debug=True)



