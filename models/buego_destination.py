from odoo import models, fields, api

class BuegoDestination(models.Model):
    _name = 'buego.destination'
    _rec_name = 'name'
    _order = 'date_localization desc, start_datetime desc'

    name = fields.Char("Name")
    start_datetime = fields.Datetime("Start Date")
    end_datetime = fields.Datetime("End Date")
    location_id = fields.Many2one("buego.location","Location")
    latitude = fields.Float(related='location_id.latitude')
    longitude = fields.Float(related='location_id.longitude')
    partner_id = fields.Many2one("res.partner", "Partner")
    date_localization = fields.Date("Date")