# Copyright 2020 Odoo S.A. (https://odoo.com)
# Copyright 2020 Opener B.V. (https://opener.amsterdam)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestSurveyValueImage(TransactionCase):
    def test_survey_value_image(self):
        """ Image can not be set if not allowed in the question settings """
        answer = self.env.ref('survey.choice_1_1_1')
        answer.value_image = False

        answer.question_id.allow_value_image = False
        with self.assertRaises(ValidationError):
            answer.value_image = (
                "R0lGODdhAQABAIAAAP///////ywAAAAAAQABAAACAkQBADs=")

        answer.question_id.allow_value_image = True
        answer.value_image = (
            "R0lGODdhAQABAIAAAP///////ywAAAAAAQABAAACAkQBADs=")
