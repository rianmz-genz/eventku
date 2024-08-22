import json
from odoo.http import Response

def make_json(raw):
    return json.dumps(raw)

def base_format(data, message):
    return {
        'message': message,
        'data': data
    }

def response_json(raw_data, message, status=200):
    return Response(make_json(base_format(data=raw_data,message=message)), content_type='application/json', status=status)
