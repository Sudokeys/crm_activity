# -*- coding: utf-8 -*-

{
    "name": 'crm_activity_meeting',
    "version": "0.1",
    "depends": [
        'base',
        'crm_activity',
        'crm',
    ],
    "author": "Nicolas JEUDY",
    "category": "Tools",
    "installable" : True,
    "auto_installable": False,
    "data": [
        'view/view.xml',
        'view/ir_ui_view_record.xml',
        'crm_activity_type_record.xml',
        'crm_activity_end_result_record.xml',
    ],
}
