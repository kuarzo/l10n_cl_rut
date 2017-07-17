# -*- coding: utf-8 -*-
from odoo import http

# class L10nClRut(http.Controller):
#     @http.route('/l10n_cl_rut/l10n_cl_rut/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_rut/l10n_cl_rut/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_rut.listing', {
#             'root': '/l10n_cl_rut/l10n_cl_rut',
#             'objects': http.request.env['l10n_cl_rut.l10n_cl_rut'].search([]),
#         })

#     @http.route('/l10n_cl_rut/l10n_cl_rut/objects/<model("l10n_cl_rut.l10n_cl_rut"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_rut.object', {
#             'object': obj
#         })