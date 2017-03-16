# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging

class hr_candidate_type(models.Model):
    _name = 'hr.candidate.type'        
    
    name = fields.Char(string="Candidate Type")