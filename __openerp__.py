# -*- coding: utf-8 -*-
{
    'name': "hr_ext_qa",

    'summary': """
        Adds different fields to suit special demands
""",

    'description': """
        Adds different fields to suit special demands
    """,

    'author': "Simbioz, yustas147",
    'website': "http://simbioz.odooua.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_recruitment'],

    # always loaded
    'data': [
#        'security/ir.model.access.csv',
     #   'templates.xml',
        'views/inherited_hr_view_hr_job_form.xml',
        'views/inherited_hr_recruitment_crm_case_form_view_job.xml',
        'views/inherited_hr_view_employee_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
     #   'demo.xml',
    ],
}
