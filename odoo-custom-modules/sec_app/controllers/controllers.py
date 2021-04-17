# -*- coding: utf-8 -*-
# from odoo import http


# class SecApp(http.Controller):
#     @http.route('/sec_app/sec_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sec_app/sec_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sec_app.listing', {
#             'root': '/sec_app/sec_app',
#             'objects': http.request.env['sec_app.sec_app'].search([]),
#         })

#     @http.route('/sec_app/sec_app/objects/<model("sec_app.sec_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sec_app.object', {
#             'object': obj
#         })
