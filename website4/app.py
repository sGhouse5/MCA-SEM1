from flask import Flask, jsonify

data = {
    1 : {
        "name" : "SGM",
        "price" : 8999
    },
    2 : {
        "name" : "gg",
        "price" : 678
    },
3 : {
        "name" : "jdjd",
        "price" : 34567
    }
}

app = Flask(__name__)

@app.route('/store')
def this():
    return 'this is storrrrre'

@app.route('/search/<int:see>')
def searching(see):
    if see == 1:
        return jsonify(data[see]["name"], data[see]['price'])
    elif see == 2:
        return jsonify(data[see])
    elif see == 3:
        return jsonify(data[see])
    
if __name__ == "__main__":
    app.run(debug=True)
