from odoo import models, fields, api

class BueGoDashboard(models.Model):
    _name = 'buego.dashboard'

    name = fields.Char()