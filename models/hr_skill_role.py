# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hr_skill_role(models.Model):
    _name = 'hr.skill.role'    
    
    name = fields.Char(string='Role Name')
    skill_ids = fields.Many2many(string="Skills", comodel_name='hr.skill', relation='hr_roles_skills')