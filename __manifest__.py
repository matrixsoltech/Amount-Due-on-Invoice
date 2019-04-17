# -*- coding: utf-8 -*-
{
    'name': "Max amount due",

    'summary': """
        This program helps you determine the customer's credit limit when creating the invoice.
         Create BY MMatrix Solution Technology.
        """,

    'description': """
        Set maximum amount due per customer
    """,

    'author': "Matrix Solution Technology",
    'website': "http://matrixsoltech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}