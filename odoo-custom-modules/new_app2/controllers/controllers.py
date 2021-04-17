# -*- coding: utf-8 -*-
# from odoo import http


# class NewApp2(http.Controller):
#     @http.route('/new_app2/new_app2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_app2/new_app2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_app2.listing', {
#             'root': '/new_app2/new_app2',
#             'objects': http.request.env['new_app2.new_app2'].search([]),
#         })

#     @http.route('/new_app2/new_app2/objects/<model("new_app2.new_app2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_app2.object', {
#             'object': obj
#         })\
