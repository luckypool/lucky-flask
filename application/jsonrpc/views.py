from flask import Module, jsonify, request

jsonrpc = Module(__name__, "jsonrpc")

@jsonrpc.route("/",methods=['POST', 'GET'])
def root():
    asign_params = {
        'page_title' : 'frontend.index',
        'one' : 'hello',
        'two' : 'world'
    }
    print asign_params
    return jsonify(asign_params)

