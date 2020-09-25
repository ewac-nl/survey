# Copyright 2020 Stefan Rijnhart <stefan@opener.amsterdam>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from base64 import b64encode
from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools.translate import _


class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input_line'

    answer_type = fields.Selection(selection_add=[('binary', 'File Upload')])
    value_binary = fields.Binary('Uploaded file')
    value_binary_filename = fields.Char('File name')

    @api.model
    def save_line_binary(self, user_input_id, question, post, answer_tag):
        """ Decode the submitted FileStorage object, unless the review tag is
        set. This means that the user reviewed a previous page and submitted
        the answer unmodified. """
        vals = {
            'user_input_id': user_input_id,
            'question_id': question.id,
            'survey_id': question.survey_id.id,
            'skipped': False,
        }
        if post.get('review_%s' % answer_tag):
            # Previous answer
            return True
        if post.get(answer_tag):
            storage = post[answer_tag]
            vals.update({
                'answer_type': 'binary',
                'value_binary': b64encode(storage.read()),
                'value_binary_filename': storage.filename,
            })
        else:
            vals.update({
                'answer_type': None,
                'skipped': True,
                'value_binary': False,
                'value_binary_filename': False,
            })
        old_uil = self.search([
            ('user_input_id', '=', user_input_id),
            ('survey_id', '=', question.survey_id.id),
            ('question_id', '=', question.id)
        ])
        if old_uil:
            old_uil.write(vals)
        else:
            old_uil.create(vals)
        return True

    @api.multi
    def _check_answer_type(self):
        """ Implement the answer type check for binary answers """
        for uil in self.filtered(
                lambda uil: uil.answer_type == 'binary'):
            if not uil.value_binary:
                raise ValidationError(
                    _('A file needs to be provided in binary type answers'))
            if not uil.value_binary_filename:
                raise ValidationError(
                    _('A filename needs to be provided in binary type '
                      'answers'))
        return super(SurveyUserInputLine, self.filtered(
            lambda uil: uil.answer_type != 'binary'))._check_answer_type()
