{
    'name': 'National ID Application',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Process online applications for national IDs',
    'sequence': -100,
    'description': """This module allows for the submission and processing of national ID applications.""",
    'depends': ['base', 'mail', 'web'],
    "data": [
        "security/ir.model.access.csv",
        "views/national_id_application_views.xml",
        "report/national_id_application_report.xml"
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}