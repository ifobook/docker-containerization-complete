from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Containerization Project</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f3f6fb;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: white;
                padding: 50px;
                border-radius: 16px;
                box-shadow: 0 10px 30px #0001;
                text-align: center;
            }
            h1 { color: #1769aa; }
            p { color: #555; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Docker Containerization Complete!</h1>
            <p>Flask application successfully running inside Docker.</p>
            <p>DevOps Project | Docker + Python + Flask</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy", service="flask-docker-app")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
