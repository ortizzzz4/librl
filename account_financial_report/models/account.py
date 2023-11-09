# © 2011 Guewen Baconnier (Camptocamp)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).-
from odoo import fields, models,api


class AccountAccount(models.Model):
    _inherit = "account.account"

    centralized = fields.Boolean(string="Centralizado por dias",help="Si es true agrupara por fecha",
                                default=True)

    debit_positive = fields.Boolean(
        string="Balance Actual Positivo",
        help="Solo para cuentas que empiezan con 2, 3 o 5",
        compute='_compute_debit_positive',
        store=True,
        readonly=True
    )
    
    @api.depends('code')
    def _compute_debit_positive(self):
        for account in self:
            if account.code and account.code[0] in ['2', '3', '5']:
                account.debit_positive = True
            else:
                account.debit_positive = False