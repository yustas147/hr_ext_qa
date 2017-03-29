# -*- coding: utf-8 -*-

from openerp import models, fields, api
#import logging

#_logger = logging.getLogger(name='YUSTAS')

class res_partner(models.Model):
    _name = 'res.partner'    
    _inherit = 'res.partner'    
    
    slack = fields.Char(string="Slack")    
    application_ids = fields.One2many(comodel_name='hr.applicant',
                                      inverse_name='partner_id',
                                      string='Applications')