# -*- coding: utf-8 -*-
# from odoo import http


# class CollegePortal(http.Controller):
#     @http.route('/college_portal/college_portal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/college_portal/college_portal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('college_portal.listing', {
#             'root': '/college_portal/college_portal',
#             'objects': http.request.env['college_portal.college_portal'].search([]),
#         })

#     @http.route('/college_portal/college_portal/objects/<model("college_portal.college_portal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('college_portal.object', {
#             'object': obj
#         })
