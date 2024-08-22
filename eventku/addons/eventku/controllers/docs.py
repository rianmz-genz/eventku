# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import logging

logger = logging.getLogger(__name__)

class ProductController(http.Controller):

    @http.route('/api/docs', auth='none', website=True)
    def swagger_ui(self, **kw):
        return request.render('eventku.swagger_ui')