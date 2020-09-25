# Copyright 2020 Odoo S.A. (https://odoo.com)
# Copyright 2020 Opener B.V. (https://opener.amsterdam)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Survey: add images to multiple choice answers",
    "summary": "Add images to multiple choice answers in surveys",
    "version": "10.0.1.0.0",
    "development_status": "Beta",
    "category": "Survey",
    "website": "https://github.com/OCA/survey",
    "author": "Odoo S.A., Opener B.V., Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "survey",
        "web_tree_image",
    ],
    "data": [
        "views/survey_templates.xml",
        "views/survey_question.xml",
    ],
}
