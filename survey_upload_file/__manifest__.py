# Copyright 2020 Stefan Rijnhart <stefan@opener.amsterdam>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Upload files in surveys",
    "summary": "Survey question type to upload a file",
    "version": "10.0.1.0.0",
    "development_status": "Beta",
    "category": "Survey",
    "website": "https://github.com/OCA/survey",
    "author": "Opener B.V., Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "survey",
    ],
    "data": [
        "views/survey_question.xml",
        "views/survey_templates.xml",
        "views/survey_user_input_line.xml",
    ],
}
