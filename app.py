from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/mypost', methods=['GET'])
def getMemoPage():
    return render_template("memo.html")

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)