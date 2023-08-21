from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    reasons_discrepancies = fields.Selection(string='Reasons for discrepancies',
                                             selection=[('company_address_false', 'Company address is false'),
                                                        ('not_correct_vat_id', 'Not correct VAT ID'),
                                                        ('0_vat_rate',
                                                         'The invoice should have a 0% VAT rate, reversed charge'),
                                                        ('19_vat_rate', 'The invoice should have a 19% VAT rate'),
                                                        ('wrong_invoice_amount', 'Wrong invoice amount'),
                                                        ('made_out_in_euros', 'The invoice must be made out in euros'),
                                                        ('proof_of_delivery_false', 'Proof of delivery is false'),
                                                        ('proof_of_delivery_not_readable',
                                                         'Proof of delivery is not readable'),
                                                        ('proof_of_delivery_missing', 'Proof of delivery is missing')])