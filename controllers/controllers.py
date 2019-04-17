# -*- coding: utf-8 -*-
from odoo import http

# class AccMS(http.Controller):
#     @http.route('/acc_m_s/acc_m_s/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/acc_m_s/acc_m_s/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('acc_m_s.listing', {
#             'root': '/acc_m_s/acc_m_s',
#             'objects': http.request.env['acc_m_s.acc_m_s'].search([]),
#         })

#     @http.route('/acc_m_s/acc_m_s/objects/<model("acc_m_s.acc_m_s"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('acc_m_s.object', {
#             'object': obj
#         })