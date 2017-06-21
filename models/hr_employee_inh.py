# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class hr_employee(models.Model):
    _name = 'hr.employee'    
    _inherit = 'hr.employee'        
    
    @api.one
    def _compute_trial_start(self):
        contract = self.env['hr.contract'].search([('employee_id','=',self.name)])
        if len(contract)==1:
            _logger.info('777777777777777777777777777777 %s', contract.trial_date_start)
            self.trial_date_start = contract.trial_date_start
    
    @api.one
    def _compute_trial_end(self):
        contract = self.env['hr.contract'].search([('employee_id','=',self.name)])
        if len(contract)==1:
            _logger.info('777777777777777777777777777777 %s', contract.trial_date_end)
            self.trial_date_end = contract.trial_date_end

    def onchange_address_id(self, cr, uid, ids, address, context=None):
        return {'value': {}}
    
    mobile = fields.Char(string="Mobile", related='address_home_id.mobile')
    private_email = fields.Char(string="Private Email", related='address_home_id.email')
    education = fields.Text(string="Education")
    passport_data = fields.Text(string="Passport Data")
    city = fields.Char(string="City", related='address_home_id.parent_id.city')
    corporate_email = fields.Char(string="Corporate Email", related='user_id.login')
   # propiska = fields.Char
    last_name_ru = fields.Char(string="Last Name Ru")
    first_name_ru = fields.Char(string="First Name Ru")
    middle_name_ru = fields.Char(string="Middle Name Ru")
    nickname = fields.Char(string="Nickname")
    icq = fields.Char(string="Icq")
    
#we take these values from hr_applicant when create an employee or so
    degree = fields.Char(string="Degree")
    candidate_level = fields.Selection(string="Candidate Level", selection=[('intern','Intern'),('junior','Junior'),('upper_junior','Upper Junior'),('pre_middle','Pre-Middle'),('middle','Middle'),('upper_middle','Upper Middle'),('senior','Senior')], required=False)    
    part_time = fields.Boolean(string="Part Time")
    is_relocatable = fields.Boolean(string="Is Relocatable")        
    remote_work = fields.Boolean(string="Remote Work")
    #hr_employee_skill_data_ids
    role_ids = fields.Many2many(string='Skill Data', comodel_name='hr.skill.role', related='job_id.role_ids')
    
    trial_date_start = fields.Date('Trial Start Date', compute = _compute_trial_start)
    trial_date_end = fields.Date('Trial End Date', compute = _compute_trial_end)
    phone = fields.Char(string="Phone", related = 'address_home_id.phone', store=True)