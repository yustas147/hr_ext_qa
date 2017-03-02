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