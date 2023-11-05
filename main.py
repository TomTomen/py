from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
  return """
    <html>
        <body>
            <iframe src="https://ohio.pythonanywhere.com" style="width: 100%; height: 100vh; border: none;"></iframe>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run()
