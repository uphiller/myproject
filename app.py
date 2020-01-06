from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/mypost', methods=['GET'])
def getMemoPage():
    return render_template("index.html")

@app.route('/sign', methods=['GET'])
def listing():
    name = request.args.get('name')
    password = request.args.get('password')

    #sign = db.sign.find_one({'name': name , 'password': password}, {'_id': 0})


    return jsonify({'result': 'success'})

@app.route('/', methods=['GET'])
def index():
    return render_template("memo.html")


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)