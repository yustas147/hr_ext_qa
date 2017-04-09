# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging

_logger = logging.getLogger(name='YUSTAS')

class project_project(models.Model):
    _name = 'project.project'    
    _inherit = 'project.project'        
    
    job_ids = fields.One2many(string='Jobs', comodel_name='hr.job', inverse_name='project_id')
    job_count = fields.Integer(string='Job Count', compute='_get_job_count')    
    
    @api.multi    
    def _get_job_count(self):
        self.job_count = len(self.job_ids.mapped('id'))        
        _logger.info('job count is %s', unicode(self.job_count))
        return self.job_count
