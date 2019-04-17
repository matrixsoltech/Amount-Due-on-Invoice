# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import except_orm, Warning

#inherit table res partner{
# insert 2 field }
class AccMS(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    total_amount_due = fields.Float(compute='_residual', string="Total Amount Due")
    maximum_amount_due = fields.Float(string="Maximum Amount Due")

    @api.one
    def _residual(self):
        select_record = self.env['account.invoice'].search([('partner_id', '=', self.id)])
        currentvalue = 0
        for x in select_record:
            currentvalue = currentvalue + x.residual
        self.total_amount_due = currentvalue

# Inherit table Account Invoice,{
# insert 2 field ,
# set action }
class AccMSAccInvoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    total_amount_due = fields.Float(related='partner_id.total_amount_due', readonly=True, string='Total Amount Due')
    maximum_amount_due = fields.Float(related='partner_id.maximum_amount_due', readonly=True, string='Maximum Amount Due')

    @api.onchange('amount_total')
    def fun_amount_total(self):
        if self.amount_total > self.maximum_amount_due - self.total_amount_due:
            raise Warning((
                "Sorry this customer has exceeded the specified limit, please check with the manager "
                          ))

