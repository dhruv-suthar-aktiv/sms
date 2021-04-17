from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    api_key = fields.Char()

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param(
            "api_key", self.api_key)  #
        res = super(ResConfigSettings, self).set_values()

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()

        res['api_key'] = self.env['ir.config_parameter'].sudo(
        ).get_param('api_key')

        return res


class MailResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    mail_template_id = fields.Many2one('mail.template')

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param(
            "mail_template_id", self.mail_template_id.id)  #
        res = super(ResConfigSettings, self).set_values()

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()

    #     res['mail_template_id'] = self.env['ir.config_parameter'].sudo(
    #     ).get_param('mail_template_id')

    #     return res
