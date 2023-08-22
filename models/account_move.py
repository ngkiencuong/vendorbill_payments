from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    reasons_discrpc_id = fields.Many2one('reason.discrepancies', string='Reasons for Discrepancies')
