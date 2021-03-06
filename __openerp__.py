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
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','hr_recruitment','crm_lead_website_social', 'web_ckeditor4', 'hr_skills_extended','project_wbs'],

    # always loaded
    'data': [
#        'security/ir.model.access.csv',
     #   'templates.xml',
        'data/view_disable.xml',
        'views/inherited_hr_view_hr_job_form.xml',
        'views/inherited_hr_recruitment_crm_case_form_view_job.xml',
        'views/inherited_hr_view_employee_form.xml',
        'views/inherited_base_view_partner_form.xml',
        'views/inherited_base_res_partner_kanban_view.xml',
        'views/inherited_view_crm_lead_website_social_form1.xml',
        'views/hr_candidate_type_view.xml',
        'views/hr_skill_role.xml',
        'views/partner_applicant_menu_action.xml',
        'views/inh_base_view_partner_tree.xml',
        'views/inh_project_edit_project.xml',
        'views/inh_crm_crm_case_form_view_oppor.xml',
        'views/inh_hr_skilL_view_employee_skill_form.xml',
        'views/hr_job_skill_data.xml',
        'views/inherited_hr_view_employee_filter.xml',
        'data/hr.applicant_category.csv',
        'data/hr.candidate.type.csv',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
     #   'demo.xml',
    ],
}
# removed 
#        'views/Candidate_menu_action.xml',
