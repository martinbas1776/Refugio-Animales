# -*- coding: utf-8 -*-
# from odoo import http


# class RefugioAnimales(http.Controller):
#     @http.route('/refugio_animales/refugio_animales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/refugio_animales/refugio_animales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('refugio_animales.listing', {
#             'root': '/refugio_animales/refugio_animales',
#             'objects': http.request.env['refugio_animales.refugio_animales'].search([]),
#         })

#     @http.route('/refugio_animales/refugio_animales/objects/<model("refugio_animales.refugio_animales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('refugio_animales.object', {
#             'object': obj
#         })

