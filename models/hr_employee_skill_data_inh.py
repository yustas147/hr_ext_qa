# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging

_logger = logging.getLogger(name='YUSTAS')


class hr_employee_skill_data_inh(models.Model):
    _name = 'hr.employee.skill.data'    
    _inherit = 'hr.employee.skill.data'
    
    applicant_id = fields.Many2one(comodel_name='hr.applicant', string=None)
    
    @api.model
    def sync_skills(self,obj):
        _logger.info('self is %s' % (unicode(self)))
        emp = obj.employee_id
        appl = obj.applicant_id
#        emp.update({"skill_ids":[(4,obj.skill_id.id)]})
        if emp:
            sk_ids = emp.hr_employee_skill_data_ids.mapped('skill_id').mapped('id')
            _logger.info('from sync_skills: sk_ids is %s' % (sk_ids)) 
            emp.update({"skill_ids":[(6,0,sk_ids)]})    
        if appl:
            sk_ids = appl.skill_data_ids.mapped('skill_id').mapped('id')
            _logger.info('from sync_skills: sk_ids is %s' % (sk_ids)) 
            appl.update({"skill_ids":[(6,0,sk_ids)]})    