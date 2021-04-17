

# -*- coding: utf-8 -*-
{
    'name': "NewApp",

    'summary': """
        This is a NewApp """,

    'description': """
        Short description of module's purpose of NewApp
    """,

    'author': "NewApp Company",
    'website': "http://www.newcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'new_app2', 'course__portal', 'hr', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/course_lines.xml',
        'views/student_detail.xml',
        'views/student_xapth_demo.xml',
        'views/professor_detail.xml',
        'views/employee_document_detail.xml',
        'wizard/student_fees_wizard_view.xml',
        'wizard/student_courses_wizard_view.xml',
        'wizard/student_activity_wizard_view.xml',
        'views/res_config_settings_view.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'installable': True,
    # 'application': True,
    'auto_install': False
}
