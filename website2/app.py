from flask import Flask 
#from tap import trying
app = Flask(__name__)

@app.route('/')
def home():
    return "🏠 Welcome Home!"

@app.route('/about')
def about():
    return "📖 About Us: We teach Python!"

@app.route('/contact')
def contact():
    return "📧 Contact: email@example.com"

@app.route('/blog')
def blog():
    return '''
    <h1>Bolg page</h1>
    <p>This is blog page<p>'''

if __name__ == '__main__':
    app.run(debug=True)