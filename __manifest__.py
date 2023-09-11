{
    'name': "Vendor Payment Enhancement",
    'summary': "Vendor Payment Enhancement Module",
    'version': '16.0.1.0.0',
    'author': "Simplify-ERP™",
    'category': 'Accounting',
    'website': 'https://simplify-erp.com',
    'license': 'LGPL-3',
    'depends': ["account", "account_banking_sepa_credit_transfer"],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/account_move_views.xml',
        'views/reason_discrepancies.xml',
    ],
    'auto_install': False,
    'installable': True,
}