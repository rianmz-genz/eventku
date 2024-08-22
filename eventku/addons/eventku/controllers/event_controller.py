# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from ..helpers.response import response_json
from ..helpers.request import extract_fields_from_request, extract_multipart_fields

class EventController(http.Controller):
    
    @http.route('/api/events/', auth='none', type='http', csrf=False, methods=['POST'])
    def create_event(self, **kw):
        try:
            data = extract_fields_from_request(request.httprequest.data, [
                'name', 
                'date_time',
                'date_begin', 
                'organizer_id', 
                'address_id', 
                'date_tz',
                'seats_limited',
                'seats_max'
                ])
            
            [raw_data, message] = login_service(request=request, data=data)
            return response_json(raw_data=raw_data, message=message)
        except Exception as e:
            return response_json(raw_data={}, message=f"{e}", status=400)


