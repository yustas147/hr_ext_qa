# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging

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
                rec.name = 'Not in deparment /'
            if (rec.job_id.name):
                rec.name += rec.job_id.name            
            _logger.info('running on is  %s', unicode(rec))
        return True        
        
    
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
    priority = fields.Selection(selection=AVAILABLE_PRIORITIES, string='Appreciation')
    remote_work = fields.Boolean(string="Remote Work")
    part_time = fields.Boolean(string="Part Time")
    is_relocatable = fields.Boolean(string="Is Relocatable")
    #sale_manager = fields.Many2one(comodel_name='res.users', string='Sale Manager')
    
