import app
from flask import Flask
print("Inside tap.py, __name__ =", __name__)


man = Flask(__name__)
@man.route('/')
def trying():
        return "Why this man"
    
if __name__ == "__main__":
    man.run(debug=True)
