from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CI/CD Kubernetes Project</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 100px;">
        <h1>Hello from Version 1</h1>
        <p>CI/CD Kubernetes Demo</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
