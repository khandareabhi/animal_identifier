from flask import Flask

# Create Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello, your Render deployment is working!"

if __name__ == "__main__":
    # Needed when running locally
    app.run(host="0.0.0.0", port=8080)
