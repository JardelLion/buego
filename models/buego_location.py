from odoo import models, fields, api

class BuegoLocation(models.Model):
    _name = 'buego.location'

    name = fields.Char("Name", default='Location')
    latitude = fields.Float(digits=(16,7))
    longitude = fields.Float(digits=(16,7))