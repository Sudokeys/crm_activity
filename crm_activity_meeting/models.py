# -*- coding: utf-8 -*-

import logging

from openerp import models, api

_logger = logging.getLogger(__name__)


class crm_lead(models.Model):

    """ Model for CRM meetings """
    _name = 'crm.lead'
    _inherit = 'crm.lead'

    @api.multi
    def action_schedule_meeting(self):
        """
        Open meeting's calendar view to schedule crm_activity_meeting on
        current opportunity.

        :return dict: dictionary value for created Meeting view
        """
        lead = self
        activity_type_id = self.env.ref(
            'crm_activity_meeting.crm_activity_type_new_meeting_r0').id
        res = self.env.ref('crm_activity_meeting.action_crm_activity_meetings')
        partner_ids = [self.env['res.users'].browse(self._uid).partner_id.id]
        if lead.partner_id:
            partner_ids.append(lead.partner_id.id)
        res['context'] = {
            'default_opportunity_id': lead.type == 'opportunity'
            and lead.id or False,
            'default_partner_id': lead.partner_id.id,
            'default_partner_ids': partner_ids,
            'default_team_id': lead.team_id.id,
            'default_name': lead.name,
            'default_activity_type_id': activity_type_id,
            'search_default_opportunity_id': lead.id,
            'search_default_activity_type_id': activity_type_id,
        }
        return {
            'name': "Crm activity: Meetings",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'kanban,tree,form',
            'res_model': res.res_model,
            'views': [[False, "kanban"], [False, "tree"], [False, "form"]],
            'view_id': False,
            'context': res['context'],
        }
