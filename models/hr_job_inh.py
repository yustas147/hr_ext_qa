# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hr_job(models.Model):
    _name = 'hr.job'    
    _inherit = 'hr.job'    
    
    start_date = fields.Date(string="Start date")
    time_to_expire = fields.Date(string="Time to expire")
    time_to_expire = fields.Selection(string="Priority", selection=[('normal','Normal'),('high','High'),('very_high','Very High')])    
    step_technologies = fields.Text(string="Step Technologies")
    phase_proj_prod = fields.Selection(string="Phase project/product", selection=[('new','New'),('existing','Existing'),('other','Other')])    
    team_size = fields.Integer(string="Team size")