# -*- coding: utf-8 -*-
# from odoo import http


# class Lab2(http.Controller):
#     @http.route('/lab2/lab2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lab2/lab2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lab2.listing', {
#             'root': '/lab2/lab2',
#             'objects': http.request.env['lab2.lab2'].search([]),
#         })

#     @http.route('/lab2/lab2/objects/<model("lab2.lab2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lab2.object', {
#             'object': obj
#         })
