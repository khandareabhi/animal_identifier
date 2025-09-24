from flask import Flask

# Create the Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Render deployment is working! Your Flask app is live."

if __name__ == "__main__":
    # For local testing
    app.run(host="0.0.0.0", port=8080)
