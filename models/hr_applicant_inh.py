# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
from openerp.osv import osv
from openerp.tools.translate import _

_logger = logging.getLogger(name='YUSTAS')

AVAILABLE_PRIORITIES = [
    ('0', 'Bad'),
    ('1', 'Below Average'),
    ('2', 'Average'),
    ('3', 'Good'),
    ('4', 'Excellent'),
    ('5', 'Fantastic')
]


class hr_applicant(models.Model):
    _name = 'hr.applicant'    
    _inherit = 'hr.applicant'    
    
    @api.depends('department_id','job_id')
    def _get_applicant_name(self):
        _logger.info('self is  %s', unicode(self))
        for rec in self:
            _logger.info('rec.department_id.name is  %s', unicode(rec.department_id.name))
            _logger.info('rec.job_id.name is  %s', unicode(rec.job_id.name))
            if (rec.department_id.name):
                rec.name = rec.department_id.name + ' / '
            else:
                rec.name = ''
 #               rec.name = 'Not in deparment /'
            if (rec.job_id.name):
                rec.name += rec.job_id.name            
            _logger.info('running on is  %s', unicode(rec))
        return True        
        
    
    def create_employee_from_applicant(self, cr, uid, ids, context=None):
        """ Create an hr.employee from the hr.applicants """
        if context is None:
            context = {}
        hr_employee = self.pool.get('hr.employee')
        model_data = self.pool.get('ir.model.data')
        act_window = self.pool.get('ir.actions.act_window')
        emp_id = False
        for applicant in self.browse(cr, uid, ids, context=context):
            address_id = contact_name = False
            if applicant.partner_id:
                address_id = self.pool.get('res.partner').address_get(cr, uid, [applicant.partner_id.id], ['contact'])['contact']
                contact_name = self.pool.get('res.partner').name_get(cr, uid, [applicant.partner_id.id])[0][1]
            if applicant.job_id and (applicant.partner_name or contact_name):
                applicant.job_id.write({'no_of_hired_employee': applicant.job_id.no_of_hired_employee + 1})
                create_ctx = dict(context, mail_broadcast=True)
                a_sk_tuples = [ (4, rec.id) for rec in applicant.skill_data_ids ]
                emp_id = hr_employee.create(cr, uid, {'name': applicant.partner_name or contact_name,
                                                     'job_id': applicant.job_id.id,
                                                     'address_home_id': address_id,
                                                     'department_id': applicant.department_id.id or False,
                                                     'address_id': applicant.company_id and applicant.company_id.partner_id and applicant.company_id.partner_id.id or False,
                                                     'work_email': applicant.department_id and applicant.department_id.company_id and applicant.department_id.company_id.email or False,
                                                     'work_phone': applicant.department_id and applicant.department_id.company_id and applicant.department_id.company_id.phone or False,
                                                     'candidate_level': applicant.candidate_level,
                                                     'is_relocatable': applicant.is_relocatable,
                                                     'part_time': applicant.part_time,
                                                     'remote_work': applicant.remote_work,
                                                     
                                                     }, context=create_ctx)
                hr_employee.write(cr, uid, [emp_id], {'hr_employee_skill_data_ids': a_sk_tuples})
                self.write(cr, uid, [applicant.id], {'emp_id': emp_id}, context=context)
                self.pool['hr.job'].message_post(
                    cr, uid, [applicant.job_id.id],
                    body=_('New Employee %s Hired') % applicant.partner_name if applicant.partner_name else applicant.name,
                    subtype="hr_recruitment.mt_job_applicant_hired", context=context)
            else:
                raise osv.except_osv(_('Warning!'), _('You must define an Applied Job and a Contact Name for this applicant.'))

        action_model, action_id = model_data.get_object_reference(cr, uid, 'hr', 'open_view_employee_list')
        dict_act_window = act_window.read(cr, uid, [action_id], [])[0]
        if emp_id:
            dict_act_window['res_id'] = emp_id
        dict_act_window['view_mode'] = 'form,tree'
        return dict_act_window    
    
    name = fields.Char('Subject / Application Name', compute = '_get_applicant_name', required=False)
    
    candidate_level = fields.Selection(string="Candidate Level", selection=[('intern','Intern'),('junior','Junior'),('upper_junior','Upper Junior'),('pre_middle','Pre-Middle'),('middle','Middle'),('upper_middle','Upper Middle'),('senior','Senior')], required=True)
#    candidate_level = fields.Selection(string="Candidate Level", selection=[('normal','Normal'),('high','High'),('very_high','Very High')])
    candidate_type = fields.Many2one(string="Candidate Type", comodel_name="hr.candidate.type")
    #candidate_type = fields.Selection(string="Candidate Type", selection=[('normal','Normal'),('high','High'),('very_high','Very High')], required=True)
    current_salary = fields.Float(string="Current Salary")
    current_salary_extra = fields.Char(string="Current Salary Extra")
    availability_date = fields.Date(string="Available From")
    #skype = fields.Char(string="Skype")
    skype = fields.Char(string="Skype", related='partner_id.skype')
    slack = fields.Char(string="Slack", related='partner_id.slack')
    website = fields.Char(string="Website", related='partner_id.website')
    linkedin = fields.Char(string="Linkedin", related='partner_id.linkedin')
    facebook = fields.Char(string="Facebook", related='partner_id.facebook')
    priority = fields.Selection(selection=AVAILABLE_PRIORITIES, string='Appreciation')
    remote_work = fields.Boolean(string="Remote Work")
    part_time = fields.Boolean(string="Part Time")
    is_relocatable = fields.Boolean(string="Is Relocatable")
    skill_data_ids = fields.One2many(string='Skill Data', comodel_name='hr.employee.skill.data', inverse_name='applicant_id')
#    skill_data_ids = fields.One2many(string='Skill Data', comodel_name='hr.employee.skill.data', related='emp_id.hr_employee_skill_data_ids')
    role_ids = fields.Many2many(string='Skill Data', comodel_name='hr.skill.role', related='job_id.role_ids')
    #sale_manager = fields.Many2one(comodel_name='res.users', string='Sale Manager')
    skill_ids = fields.Many2many(
        'hr.skill',
        'skill_applicant_rel',
        'applicant_id',
        'skill_id',
        'Skills',
        domain="[('child_ids', '=', False)]",
    )
    categ_ids = fields.Many2many('hr.employee.category', string='Tags')
