# Copyright 2020 Stefan Rijnhart <stefan@opener.amsterdam>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    type = fields.Selection(selection_add=[('binary', 'File Upload')])

    @api.model
    def validate_binary(self, post, answer_tag):
        """ Honour requiredness """
        if self.constr_mandatory and (
                not post.get(answer_tag) and
                not post.get('review_%s' % answer_tag)):
            return {answer_tag: self.constr_error_msg}
        return {}
