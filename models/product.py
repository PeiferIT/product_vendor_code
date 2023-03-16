# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.osv import expression


class ProductTemplate(models.Model):
    _inherit = "product.template"

    vendor_code = fields.Char("Vendor Code")


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', '|', ('name', operator, name), ('default_code', operator, name),'|', ('barcode', operator, name), ('vendor_code', operator, name)]
        product_id = self._search(expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid)
        return product_id
