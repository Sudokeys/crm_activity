# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools.translate import _


class crm_activity_type(models.Model):
    _name = 'crm.activity.type'

    default = fields.Boolean(string="Default ?")
    ref = fields.Char(string='Ref', translatable=False)
    name = fields.Char(string='Nom', translatable=True)
    end_result_ids = fields.One2many(comodel_name='crm.activity.end_result',
                                     inverse_name='activity_type_id',
                                     string='End results for this Type')


class crm_activity_end_result(models.Model):
    _name = 'crm.activity.end_result'

    name = fields.Char(string='Nom')
    activity_type_id = fields.Many2one(comodel_name='crm.activity.type',
                                       string='Associated model')


class crm_activity(models.Model):
    """ Model for CRM meetings """
    _name = 'calendar.event'
    _inherit = 'calendar.event'

    @api.model
    def _get_default_activity_type(self):
        d_act = self.env['crm.activity.type'].search([('default', '=', True)])
        if len(d_act) >= 1:
            return d_act[0]
        return d_act
        

    @api.onchange('is_done')
    def onchange_is_done(self):
        if self.is_done:
            self.date_done = fields.Datetime.now()
        else:
            self.date_done = False
            self.end_result = False
            self.result = False

    activity_type_id = fields.Many2one(comodel_name='crm.activity.type',
                                       string='Activity Type',
                                       default=_get_default_activity_type,
                                       required=True)
    is_done = fields.Boolean(string='Done')
    date_done = fields.Datetime(string='Done at:')
    prev_calendar_event_id = fields.Many2one(comodel_name='calendar.event',
                                             string='Previous Activity')
    end_result = fields.Many2one(comodel_name='crm.activity.end_result',
                                 string='End Result')
    result = fields.Text('Result Details')
    partner_id = fields.Many2one(comodel_name='res.partner',
                                 string='Partner')
