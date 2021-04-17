# -*- coding: utf-8 -*-
{
    'name': "Hospital App",

    'summary': """
        This is a Hospital App """,

    'description': """
        Short description of module's purpose of Hospital App
    """,

    'author': "Hospital App Company",
    'website': "http://www.hospital_dt.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'hospital_detail.xml'

    ],
    # only loaded in demonstration mode

    'installable': True,
    'application': True,
    'auto_install': False
}
