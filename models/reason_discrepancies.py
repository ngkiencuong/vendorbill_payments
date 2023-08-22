from odoo import models, fields, api, _


class ReasonDiscrepancies(models.Model):
    _name = "reason.discrepancies"
    _description = "Reasons for Discrepancies"

    name = fields.Char('Name', translate=True)

    @api.model
    def create_sample_values(self):
        values = [
            {'name': _('Company address is false')},
            {'name': _('Not correct VAT ID')},
            {'name': _('The invoice should have a 0% VAT rate, reversed charge')},
            {'name': _('The invoice should have a 19% VAT rate')},
            {'name': _('Wrong invoice amount')},
            {'name': _('The invoice must be made out in euros')},
            {'name': _('Proof of delivery is false')},
            {'name': _('Proof of delivery is not readable')},
            {'name': _('Proof of delivery is missing')},
        ]
        return self.env['reason.discrepancies'].create(values)
