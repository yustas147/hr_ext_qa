# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging

_logger = logging.getLogger(name='YUSTAS')

class crm_lead(models.Model):
    _name = 'crm.lead'    
    _inherit = 'crm.lead'        
    
    job_ids = fields.One2many(string='Jobs', comodel_name='hr.job', inverse_name='lead_id')
    job_count = fields.Integer(string='Job Count', compute='_get_job_count')    
    qa_project_id = fields.Many2one(string='Project', comodel_name='project.project')
    
    @api.multi    
    def _get_job_count(self):
        self.job_count = len(self.job_ids)        
        return self.job_count