# License OPL-1 (https://www.odoo.com/documentation/16.0/legal/licenses.html).
from odoo import models, fields


class GetPaidBills(models.TransientModel):
    _name = 'get.paid.bills'
    _description = 'Get Paid Bills'

    date_from = fields.Date(string='Date From', required=True)

    date_to = fields.Date(string='Date To', required=True)

    def action_apply(self):
        # Get all reconciles with max_date between date_from and date_to, max_date is a date of payment
        reconcile_records = self.env['account.partial.reconcile'].search([
            ('max_date', '>=', self.date_from),
            ('max_date', '<=', self.date_to),
            ('company_id', 'in', self.env.context.get('allowed_company_ids')),
        ])

        # Get all invoices from reconciles
        move_ids = reconcile_records.mapped('credit_move_id.move_id').ids

        # Return action window with invoices
        result = self.env['ir.actions.act_window']._for_xml_id('account.action_move_in_invoice_type')
        result.update({
            'domain': [
                ('id', 'in', move_ids),
                ('payment_state', 'in', ['paid', 'partial'])
            ],
        })
        return result
