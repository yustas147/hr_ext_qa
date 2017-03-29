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
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_recruitment','crm_lead_website_social', 'web_ckeditor4', 'hr_skills_extended'],

    # always loaded
    'data': [
#        'security/ir.model.access.csv',
     #   'templates.xml',
        'views/inherited_hr_view_hr_job_form.xml',
        'views/inherited_hr_recruitment_crm_case_form_view_job.xml',
        'views/inherited_hr_view_employee_form.xml',
        'views/inherited_base_view_partner_form.xml',
        'views/inherited_base_res_partner_kanban_view.xml',
        'views/inherited_view_crm_lead_website_social_form1.xml',
        'views/hr_candidate_type_view.xml',
        'views/hr_skill_role.xml',
        'data/hr.applicant_category.csv',
        'data/hr.candidate.type.csv',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
     #   'demo.xml',
    ],
}
