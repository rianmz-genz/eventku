# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from ..helpers.response import response_json
from ..helpers.request import extract_fields_from_request, extract_multipart_fields
from ..services.company_service import login_service, register_service

import logging
class CompanyController(http.Controller):
    
    @http.route('/api/login', auth='none', type='http', csrf=False, methods=['POST'])
    def login(self, **kw):
        try:
            data = extract_fields_from_request(request.httprequest.data, ['email', 'password'])
            
            [raw_data, message] = login_service(request=request, data=data)
            return response_json(raw_data=raw_data, message=message)
        except Exception as e:
            return response_json(raw_data={}, message=f"{e}", status=400)

    @http.route('/api/register', auth='none', type='http', csrf=False, methods=['POST'])
    def register(self, **kw):
        try:
            data = extract_multipart_fields(request, ['email', 'password', 'name', 'logo'])
            
            [raw_data, message] = register_service(request=request, data=data)
            return response_json(raw_data=raw_data, message=message)            
        except Exception as e:
            return response_json(raw_data={}, message=f"{e}", status=400)

