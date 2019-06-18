from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def hello():
    return 'hello world'

@app.route('/chart/', methods=['GET'])
def chart():
    return render_template('chart.html')


@app.route('/getdata/', methods=['GET'])
def get_data():
    data = {
        'x': ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"], 
        'y': [5, 20, 36, 10, 10, 20]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
#from flask import Flask
#app = Flask(__name__)
#
#@app.route('/')
#def hello_world():
#    return 'Hello World!'
#
#if __name__ == '__main__':
#    app.run()