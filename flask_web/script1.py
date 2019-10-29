from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Website Home page content"

@app.route('/about')
def about():
    return "Website About Page content"
if __name__ == "__main__":
    app.run(debug=True)