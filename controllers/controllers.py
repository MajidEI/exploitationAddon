# -*- coding: utf-8 -*-
from odoo import http

# class Explo(http.Controller):
#     @http.route('/explo/explo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/explo/explo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('explo.listing', {
#             'root': '/explo/explo',
#             'objects': http.request.env['explo.explo'].search([]),
#         })

#     @http.route('/explo/explo/objects/<model("explo.explo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('explo.object', {
#             'object': obj
#         })