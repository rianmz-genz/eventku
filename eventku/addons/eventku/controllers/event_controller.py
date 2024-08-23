# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from ..helpers.response import response_json
from ..helpers.request import extract_fields_from_request, extract_multipart_fields
from ..services.event_service import create_event_service, get_event_by_organizer_service
from .middlewares import custom_auth_required
import logging
class EventController(http.Controller):
    
    @http.route('/api/events/', auth='none', type='http', csrf=False, methods=['POST'])
    @custom_auth_required
    def create_event(self, **kw):
        try:
            data = extract_multipart_fields(request, [
                'name', 
                'date_end',
                'date_begin', 
                'date_tz',
                'seats_limited',
                'seats_max',
                'badge_image',
                ])
            logging.info(f'daaaaa{data}')
            [raw_data, message] = create_event_service(request=request, data=data)
            return response_json(raw_data=raw_data, message=message)
        except Exception as e:
            return response_json(raw_data={}, message=f"{e}", status=400)
        
    @http.route('/api/events/', auth='none', type='http', csrf=False, methods=['GET'])
    @custom_auth_required
    def get_event(self, **kw):
        try:
            [raw_data, message] = get_event_by_organizer_service(request=request)
            return response_json(raw_data=raw_data, message=message)
        except Exception as e:
            return response_json(raw_data={}, message=f"{e}", status=400)


