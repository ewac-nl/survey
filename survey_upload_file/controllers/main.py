# Copyright 2020 Stefan Rijnhart <stefan@opener.amsterdam>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import json

from odoo.addons.survey.controllers.main import WebsiteSurvey
from odoo.http import request, route


class SurveyUploadFile(WebsiteSurvey):
    @route([
        '/survey/prefill-binary/<model("survey.survey"):survey>'
        '/<string:token>',
        '/survey/prefill-binary/<model("survey.survey"):survey>'
        '/<string:token>/<model("survey.page"):page>'],
                type='http', auth='public', website=True)
    def prefill_binary(self, survey, token, page=None, **post):
        """ Set preexisting values of binary questions """
        res = {}
        domain = [('user_input_id.token', '=', token),
                  ('answer_type', '=', 'binary'),
                  ('skipped', '=', False)]
        if page:
            domain.append(('page_id', '=', page.id))
        answers = request.env['survey.user_input_line'].sudo().search(
            domain)
        if answers:
            for answer in answers:
                res['%s_%s_%s' % (
                    answer.survey_id.id, answer.page_id.id,
                    answer.question_id.id)] = answer.value_binary_filename
        return json.dumps(res)
