# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hr_employee(models.Model):
    _name = 'hr.employee'    
    _inherit = 'hr.employee'        
    
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
