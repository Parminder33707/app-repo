from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from the Fitness App (CI/CD demo)!"

@app.route("/health")
def health():
    return jsonify(status="UP"), 200

if __name__ == "__main__":
    # Bind to 0.0.0.0 so container exposes it to test
    app.run(host="0.0.0.0", port=5000)


