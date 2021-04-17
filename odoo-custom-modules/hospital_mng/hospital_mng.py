from odoo import api, fields, models


class Hospital(models.Model):
    _name = "hospital.hospital"
    _description = 'desc of Hospital mng.'

    name = fields.Char()
