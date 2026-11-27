from odoo import models, fields, api, _

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    destination_ids = fields.One2many('buego.destination', 'partner_id', string='Destinations')
    destination_count = fields.Integer("Destination Count", compute='_compute_destination_count')


    @api.depends('destination_ids')
    def _compute_destination_count(self):
        for rec in self:
            rec.destination_count = len(rec.destination_ids.ids)


    def action_destination(self):
        self.ensure_one()
        return {
            'name': _('Related Employees'),
            'type': 'ir.actions.act_window',
            'res_model': 'buego.destination',
            'view_mode': 'kanban',
            'domain': [('id', 'in', self.destination_ids.ids)]
        }