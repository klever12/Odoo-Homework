from odoo import models, fields

class Course(models.Model):
	_name = "Course.model"
	name = fields.Char(required=True)
	title = fields.Char(required=True)
	description = fields.Char()
