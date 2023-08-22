{
    'name': "Vendor Payment Enhancement",
    'summary': "Vendor Payment Enhancement Module for Odoo Version 16 Enterprise",
    'version': '16.0.1.0.0',
    'author': "Simplify-ERP™",
    'category': 'Accounting',
    'website': 'https://simplify-erp.com',
    'license': 'LGPL-3',
    'depends': ["account_accountant", "account_sepa"],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/account_move_views.xml',
        'views/reason_discrepancies.xml',
    ],
    'auto_install': False,
    'installable': True,
}