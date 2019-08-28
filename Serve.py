from flask import Flask
from flask import request,jsonify
import TSP_main as TSP
# import Test as T

app = Flask(__name__)
# @app.route("/double",methods=['POST'])
# def hello():
#     args = request.json
#     return jsonify(code = 200,status = 0,message = 'ok',data = {'value':args['value']*2})

# @app.route("/TSP",methods=['POST'])
# def TSP():
#     args = request.json
#     return jsonify(code=200,value=T.func(args['value']))

@app.route("/TTT",methods=['POST'])
def H():
    args = request.json
    return jsonify(code=200,path=TSP.start(args))
if __name__ == '__main__':
    app.run(host='192.168.10.236',port=8002,debug=True)

