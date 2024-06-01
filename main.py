from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    my_set = {"Hello World, our names are: Jeanhela Nazate,Cristhopher Villamarin and Johan Romo. We are group number 1"}
    return jsonify(list(my_set))


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))