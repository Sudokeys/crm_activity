# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.tools.translate import _


class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    @api.one
    def _count_activity(self):
        self.activity_count = len(self.crm_activity_ids)

    crm_activity_ids = fields.One2many('calendar.event', 'partner_id',
                                       'Activities', readonly=True)
    activity_count = fields.Integer(compute='_count_activity',
                                    string='Count activity')
