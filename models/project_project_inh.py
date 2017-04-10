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
        _logger.info('self is  %s', unicode(self))
        for rec in self:
            rec.job_count = len(rec.job_ids.mapped('id'))        
            _logger.info('running on is  %s', unicode(rec))
        return True
