# Copyright 2020 Odoo S.A. (https://odoo.com)
# Copyright 2020 Opener B.V. (https://opener.amsterdam)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    allow_value_image = fields.Boolean(
        'Images on answers',
        help=('Display images in addition to answer label. Valid only for '
              'simple / multiple choice questions.'))

    @api.onchange('allow_value_image')
    @api.model
    def onchange_allow_value_image(self):
        if self.allow_value_image and self.display_mode != 'columns':
            self.display_mode = 'columns'
