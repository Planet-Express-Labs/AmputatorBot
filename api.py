from flask import Flask, jsonify, request, abort
import json
import jsonschema
import os
import yaml

from basic_funcs import get_reply, get_replacement_array

with open("api_config.yml") as f:
    config=yaml.safe_load(f)

request_schema= \
{
  "message": "string",
  "required": [
    "message",
  ]
}

api=Flask(__name__)

@api.route('/api/replacementArray', methods=['POST'])
def replacement():
    req=json.loads(request.data)
    try:
        jsonschema.validate(req, request_schema)
    except:
        abort(418)
    return jsonify({'array':get_replacement_array(req['message'])})

@api.route('/api/reply', methods=['POST'])
def reply():
    req=json.loads(request.data)
    try:
        jsonschema.validate(req, request_schema)
    except:
        abort(418)
    return jsonify({'message':get_reply(req['message'])})


api.run(config['HOST'],config['PORT'], ssl_context='adhoc', debug=False)