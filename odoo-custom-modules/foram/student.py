from odoo import api, fields, models


class Foram(models.Model):
    _name = "foram.foram"
    _description = 'Foram'

    name = fields.Char()
