# Copyright 2020 Odoo S.A. (https://odoo.com)
# Copyright 2020 Opener B.V. (https://opener.amsterdam)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class SurveyLabel(models.Model):
    _inherit = 'survey.label'

    value_image = fields.Binary('Image', widget='image')

    @api.constrains('value_image')
    def check_image_allowed(self):
        for answer in self:
            if answer.value_image and not answer.question_id.allow_value_image:
                raise ValidationError(_(
                    'Images on answers are not enabled in the settings of '
                    'question "%s".' % answer.question_id.question))
        return True
