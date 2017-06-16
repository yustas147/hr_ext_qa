# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hr_job(models.Model):
    _name = 'hr.job'    
    _inherit = 'hr.job'   
    
    @api.model
    def _set_sd(self):    
        return fields.Date.context_today(self)    
    
    #start_date = fields.Date(string="Start date", default=fields.Date.context_today(self))
    start_date = fields.Date(string="Start date", required=True, default=_set_sd)
    time_to_expire = fields.Date(string="Time to expire")
    priority = fields.Selection(string="Priority", selection=[('low','Low'),('normal','Normal'),('high','High'),('very_high','Very High')])    
    step_technologies = fields.Text(string="Stack Technologies", required="True" )
#    duties = fields.Text(string="Duties", required="True")
    requirement = fields.Text(string="Requirement",  required="True")
    phase_proj_prod = fields.Selection(string="Phase project/product", selection=[('new','New'),('existing','Existing'),('other','Other')])    
    team_size = fields.Integer(string="Team size")
    remote_allowed = fields.Selection(string="Remote Allowed?", selection=[('allowed','Allowed'),('disallowed','Disallowed'),('partially_allowed','Partiallly Allowed')])    
    project_description = fields.Text(string="Project Description")    
    #application_ids = fields.Many2many(string="Applications", comodel_name="hr.applicant", relation="hr_job_applicant")        
    salesperson_id = fields.Many2one(comodel_name='res.users', string="Sale Person")    
    no_of_recruitment = fields.Selection(required=False, default=1, selection=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7')])
    #no_of_recruitment = fields.Selection(required=True, default=1, selection=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7')])
    #no_of_recruitment = fields.Integer(required=True, default=1)    
    role_ids = fields.Many2many(string='Work Roles',comodel_name='hr.skill.role',relation='hr_jobs_roles_related')    
    for_who = fields.Selection(string="Target", selection=[('Internal','Internal'),('External','External')], default='External')    
    
    project_id = fields.Many2one(string='Project', comodel_name='project.project')
    lead_id = fields.Many2one(string='Opportunity', comodel_name='crm.lead')    
    salary_from = fields.Integer(string='from')
    salary_till = fields.Integer(string='till')
    
    skill_ids = fields.Many2many(string="Skills", comodel_name='hr.skill', relation='hr_jobs_skills')    
    skill_data_ids = fields.One2many(string="Skills", comodel_name='hr.job.skill.data', inverse_name='job_id')    
    
class hr_job_skill_data(models.Model):
    _name = 'hr.job.skill.data'    
    
    #name = fields.Char('Name')
    percentage = fields.Integer(string='Grade of owning')
    description = fields.Text(string='Full skill demands description')    
    #employee_id = fields.Many2one(comodel_name='hr.employee', string=None)
    job_id = fields.Many2one(comodel_name='hr.job', string=None)
    skill_id = fields.Many2one(comodel_name='hr.skill', string='Skill Data')
#    skill_id = fields.Many2one(comodel_name='hr.skill', string=None, ondelete='cascade')
    