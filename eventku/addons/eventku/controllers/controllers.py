# -*- coding: utf-8 -*-
# from odoo import http


# class Eventku(http.Controller):
#     @http.route('/eventku/eventku', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eventku/eventku/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('eventku.listing', {
#             'root': '/eventku/eventku',
#             'objects': http.request.env['eventku.eventku'].search([]),
#         })

#     @http.route('/eventku/eventku/objects/<model("eventku.eventku"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eventku.object', {
#             'object': obj
#         })

