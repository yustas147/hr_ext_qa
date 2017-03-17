# -*- coding: utf-8 -*-

from openerp import models, fields, api
#import logging

#_logger = logging.getLogger(name='YUSTAS')

class res_partner(models.Model):
    _name = 'res.partner'    
    _inherit = 'res.partner'    
    
    slack = fields.Char(string="Slack")