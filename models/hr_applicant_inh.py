# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging

_logger = logging.getLogger(name='YUSTAS')

class hr_applicant(models.Model):
    _name = 'hr.applicant'    
    _inherit = 'hr.applicant'    
    
    candidate_level = fields.Selection(string="Candidate Level", selection=[('normal','Normal'),('high','High'),('very_high','Very High')])
    candidate_type = fields.Many2one(string="Candidate Type", comodel_name="hr.candidate.type")
#    candidate_type = fields.Selection(string="Candidate Type", selection=[('normal','Normal'),('high','High'),('very_high','Very High')])
    current_salary = fields.Float(string="Current Salary")
    availability_date = fields.Date(string="Available From")
    #skype = fields.Char(string="Skype")
    #skype = fields.Char(string="Skype", related='partner_id.skype')
    
    
