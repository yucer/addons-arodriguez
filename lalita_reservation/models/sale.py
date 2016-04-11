# -*- encoding: utf-8 -*-
##############################################################################
#
#    Custom module for Odoo
#    @author Alexander Rodriguez <adrt271988@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _

class LalitaSaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.one
    def create_reservation(self):
        values = {
                    'sale_id': self.id,
                    'partner_id': self.partner_id.id,
                    'expected_income': self.amount_total,
                    'pricelist_id': self.pricelist_id and self.pricelist_id.id or False,
                    'berths': self.berths,
                    'arrival_date': self.arrival_date and self.arrival_date[0:10] or fields.Date.today(),
                    'out_date': self.departure_date and self.departure_date[0:10] or fields.Date.today(),
                }
        reservation = self.env['lalita.reservation'].create(values)
        self.reservation_created = reservation and True or False
        #~ view_form = self.env.ref('lalita_reservation.view_form_lalita_reservation', False)
        #~ return {
            #~ 'type': 'ir.actions.act_window',
            #~ 'res_model': 'lalita.reservation',
            #~ 'res_id': reservation.id,
            #~ 'view_type': 'form',
            #~ 'views': [(view_form.id, 'form')],
            #~ 'view_mode': 'tree,form,calendar',
            #~ 'view_id': view_form.id,
            #~ 'target': 'current',
        #~ }

    #~ reservation_id = fields.Many2one('lalita.reservation', 'Reserva')
    reservation_created = fields.Boolean(string='Reserva Creada?',default=False)
